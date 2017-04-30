$(document).ready(( ) => {
  var width  = 320
  var height = 240

  Webcam.set({ width: 320, height: 240, unfreeze_snap: false })
  Webcam.attach('#webcam')

  var canvas = new fabric.Canvas('canvas')
  canvas.setWidth(width)
  canvas.setHeight(height)

  $('#btn-freeze').click(( ) => {
    Webcam.freeze()

    $('#btn-toolbar-unfreeze').addClass('hidden')
    $('#btn-toolbar-freeze').removeClass('hidden')
  })

  $('#btn-unfreeze').click(( ) => {
    Webcam.unfreeze()

    $('#webcam').removeClass('hidden')
    $('#canvas').addClass('hidden')

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
              $('#canvas').removeClass('hidden')

              canvas.add(image)

              var regions  = response.data

              for ( var i  = 0 ; i < response.data.length ; ++i ) {
                var region = regions[i]
                var rect   = region['rect']
                var digit  = region['digit'].toString()

                console.log(digit)

                console.log(region)

                var rect   = new fabric.Rect({ left: rect.x, top: rect.y,
                  width: rect.width, height: rect.height, fill: 'transparent',
                  stroke: '#9C27B0', strokeWidth: 1.5 })

                var text   = new fabric.Text(digit, { left: rect.left, top: rect.top,
                  fill: '#9C27B0' })

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
