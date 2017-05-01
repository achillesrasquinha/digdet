class Config { }

Config.App               = { }
Config.App.NAME          = 'digdet'
Config.App.CONTAINER_ID  = 'app'
Config.App.WEBCAM        = { width: 480, height: 640 }

Config.URL               = { }
Config.URL.BASE          = '/'
Config.URL.ASSETS        = `${Config.URL.BASE}assets`

Config.URL.API           = `${Config.URL.BASE}api`
Config.URL.DETECT        = `${Config.URL.API}/detect`
Config.URL.LANG          = `${Config.URL.API}/lang`

export default Config
