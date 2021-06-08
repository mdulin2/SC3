## Solutions
Cross-site scriping (XSS) is an attack where JavaScript (or HTML) can be injected into the web page.   
Because of this, an attacker can do arbitrary action as the user, steal their session cookies and do plenty of bad things.   
The goal of these challenges is to bypass the filters put in place to get XSS. In general, the input from the user is   
being concatenated with a string in an insecure way.   
  
The goal is to use the current output encoding structure against itself in order to have some control over the content of the   
JavaScript being executed. 

### Challenge 1

This content is injected directly into the DOM. So, this is the easy ``script`` injection.

Solution: `<script>alert(1)</script>`

Flag: `flag{ezpz_xss_squeezy}`

### Challenge 2

The user string is concatenated within an HTML attribute. By adding a double quote (") it is possible to escape   
the attribute to add our own attribute to get XSS. 

Solution: `" onfocus="alert(1)` (or some other event)

Flag: `flag{xss_on_event_fun_fun}`

### Challenge 3

The user string is concatenated within straight JavaScript code. By adding a single quote ('), we can escape the   
string and add our own code. 

Solution: `'); alert(1); //`

Flag: `flag{xss_sneaky_clever_fren}`

### Challenge 4
The user string is put directly into a [template string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).   
The template string has properties that allow it to run JavaScript and do other crazy things. By using the `$`,   
we can run JS in the context of the template string. 

Solution: `${alert(1)}`

Flag: `flag{xss_templeet_string}`


### Challenge 5

The user string is added directly to an iFrame source attribute. By using a JavaScript URI, the code within the link will be executed. 

Solution: `javascript:alert(1)`

Flag: `flag{iframe_shenanigans_xss}`
