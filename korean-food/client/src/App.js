import React from 'react';
import { Switch, BrowserRouter, Route } from 'react-router-dom';

import loginScreen from './loginScreen.js';
import register from './register.js';
import koreanFood from './koreanFood.js';
import './App.css';
//https://reactjs.org/docs/forms.html

const Routes = () => (
    <BrowserRouter>
        <Switch>
          <Route path='/register' component={register}/>
          <Route path='/koreanFood' component={koreanFood}/>
          <Route path='/' component={loginScreen}/>
        </Switch>
    </BrowserRouter>
);

export default Routes;
