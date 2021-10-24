from flask import Flask
from flask import render_template
from flask import request
from flask import Markup
from bs4 import BeautifulSoup
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor
import re
import json 

app = Flask(__name__)
secrets_file = open("secrets_config.json")
secrets_dict = json.load(secrets_file)

@app.route('/', methods=['POST', 'GET'])
def xss1():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']

    html = render_template('xss1.html', userInput=Markup(userInput))
    soup = BeautifulSoup(html)
    scripts = soup.find_all('script')

    flag = None
    if len(scripts) > 0:
        flag = secrets_dict['flag1']

    return render_template('xss1.html', userInput=Markup(userInput), flag=flag)

def filter_on_event(tag):
        if(tag.name != "input" or (len(tag.attrs) <= 2)):
            return False

        keys = list(tag.attrs.keys())
        print(keys) 
        for key in keys:
            if(key[0:2] == "on"):
                return True
        return False

@app.route('/xss2', methods=['POST', 'GET'])
def xss2():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']
    userInput = userInput.replace('<', '').replace('>', '')

    html = render_template('xss2.html', userInput=Markup(userInput))
    soup = BeautifulSoup(html)

    scripts = soup.findAll(filter_on_event)
    
    flag = None
    if len(scripts) > 0:

        attrs = list(scripts[0].attrs.keys())
        attr = None
        for elt in attrs:
            if(elt[0:2] == "on"):
                attr = elt
        if(attr == None):
            return render_template('xss2.html', userInput=Markup(userInput), flag=flag)
        data = scripts[0][attr]
        parser = Parser()
        tree = parser.parse(data)
        for node in nodevisitor.visit(tree):
            if 'alert(1)' in node.to_ecma():
                flag = secrets_dict['flag2']

    return render_template('xss2.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss3', methods=['POST', 'GET'])
def xss3():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']
    userInput = userInput.replace('<', '').replace('>', '').replace('"', '&quot;')

    html = render_template('xss3.html', userInput=Markup(userInput))
    soup = BeautifulSoup(html)
    scripts = soup.find_all('script')
    script = scripts[0]

    flag = None
    data = str(script).replace('<script>','').replace('</script>', '')
    parser = Parser()

    try:
        tree = parser.parse(data)
        for node in nodevisitor.visit(tree):
            if 'alert(1)' in node.to_ecma():
                flag = secrets_dict['flag3']
    except:
        pass

    return render_template('xss3.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss4', methods=['POST', 'GET'])
def xss4():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']
    userInput = userInput.replace('<', '').replace('>', '').replace('"', '').replace("'", '').replace("`", '')

    flag = None
    parser = Parser()

    try:
        matches = re.findall("\$\{(.*)?\}", userInput)
        for match in matches:
            tree = parser.parse(match)
            for node in nodevisitor.visit(tree):
                if 'alert(1)' in node.to_ecma():
                    flag = secrets_dict['flag4']
    except:
        pass

    return render_template('xss4.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss5', methods=['POST', 'GET'])
def xss5():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']

    flag = None
    parser = Parser()

    try:
        userInput = userInput.strip()
        data = ''
        if userInput.startswith('javascript:'):
            data = userInput[11:]
        tree = parser.parse(data)
        for node in nodevisitor.visit(tree):
            if 'alert(1)' in node.to_ecma():
                flag = secrets_dict['flag5']
    except:
        pass

    return render_template('xss5.html', userInput=userInput, flag=flag)
