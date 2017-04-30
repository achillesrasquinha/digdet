import React from 'react'
import ReactDOM from 'react-dom'
import { Router, browserHistory } from 'react-router'

import Config from './Config'
import Routes from './Routes'

const appRouter    = (
  <Router
    history={browserHistory}
    children={Routes}/>
)
const appContainer = $('#' + Config.App.CONTAINER_ID)[0];

ReactDOM.render(appRouter, appContainer)
