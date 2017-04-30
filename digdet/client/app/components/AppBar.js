import React from 'react'

import Config from '../Config'

class AppBar extends React.Component {
  render ( ) {
    return (
      <div className="navbar navbar-default appbar-brand navbar-static-top">
        <div className="container-fluid">
          <div className="navbar-header">
            <a className="navbar-brand">
              <div className="font-brand font-bold">
                {Config.App.NAME}
              </div>
            </a>
          </div>
          <div className="collapse navbar-collapse">
            <ul className="nav navbar-nav navbar-right">
              <li className="dropdown">
                <a className="dropdown-toggle" data-toggle="dropdown">
                  <i className="fa fa-fw fa-ellipsis-v"></i>
                </a>
                <ul className="dropdown-menu">
                  <li>
                    <a href="#">
                      About
                    </a>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </div>
    )
  }
}

export default AppBar
