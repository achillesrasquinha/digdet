var Config                 = {  }
Config.WEBCAM_MAX_WIDTH    = 320
Config.WEBCAM_MAX_HEIGHT   = 240
Config.WEBCAM_ASPECT_RATIO = Config.WEBCAM_MAX_WIDTH / Config.WEBCAM_MAX_HEIGHT

var canvas                 = new fabric.Canvas('canvas')

const renderCanvas         = () => {
  var $container = $('#canvas-container')

  var width   = Math.min(Config.WEBCAM_MAX_WIDTH, $container.width())
  var height  = width / Config.WEBCAM_ASPECT_RATIO

  Webcam.set({ width: width, height: height, unfreeze_snap: false })
  Webcam.attach('#webcam')

  canvas.setWidth(width)
  canvas.setHeight(height)
}

$(document).ready(( ) => {
  renderCanvas()
  $('.canvas-container').addClass('hidden')

  $('#btn-freeze').click(( ) => {
    Webcam.freeze()

    $('#btn-toolbar-unfreeze').addClass('hidden')
    $('#btn-toolbar-freeze').removeClass('hidden')
  })

  $('#btn-unfreeze').click(( ) => {
    Webcam.unfreeze()

    $('#webcam').removeClass('hidden')
    $('.canvas-container').addClass('hidden')

    $('#btn-toolbar-freeze').addClass('hidden')
    $('#btn-toolbar-unfreeze').removeClass('hidden')
  })

  $('#btn-detect').click(( ) => {
    Webcam.snap((data) => {
      var index  = data.indexOf(',')
      var b64str = data.substr(index + 1)
      var params = { "image": b64str }

      $.ajax({
        url: '/api/detect',
        data: params,
        type: "POST",
        success: (response)  => {
          var response = JSON.parse(response)
          var status   = response.status

          if ( status == 'success' ) {
            fabric.Image.fromURL(data, (image) => {
              $('#webcam').addClass('hidden')
              $('.canvas-container').removeClass('hidden')

              canvas.add(image)

              var regions  = response.data

              for ( var i  = 0 ; i < response.data.length ; ++i ) {
                var region = regions[i]
                var rect   = region['rect']
                var digit  = region['digit'].toString()

                var rect   = new fabric.Rect({ left: rect.x, top: rect.y,
                  width: rect.width, height: rect.height, fill: 'transparent',
                  stroke: '#9C27B0', strokeWidth: 3 })

                var text   = new fabric.Text(digit, { fontFamily: "Roboto",
                  left: rect.left, top: rect.top, fill: '#FFFFFF' })

                canvas.add(rect)
                canvas.add(text)
              }

              canvas.renderAll()
            })
          }
        },
        error: ( xhr, status ) => {

        }
      })
    })
  })
})
