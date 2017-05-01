![](.github/logo.png)
> A realtime digit OCR on the browser using Machine Learning

### Demo
![](.github/demo.gif)

You can view the demo on [https://digdet.herokuapp.com](https://digdet.herokuapp.com)

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Dependencies](#dependencies)
* [License](#license)

### Installation
Download or clone the repository as follows:

```console
$ git clone git@github.com:achillesrasquinha/digdet.git
```

Install necessary dependencies:

```console
$ make install
```

### Usage

```console
$ make all
```

Your app should now be up and running on http://localhost:5000.

#### API
Send in a base-64 encoded image string HTTP POST (with `image` as the parameter) request to [https://digdet.herokuapp.com/api/detect](https://digdet.herokuapp.com/api/detect). Let's consider a local test image:

```python
>>> import base64, requests, json, pprint
>>> with open('test.jpg', 'rb') as f:
...     buffer_ = f.read()
...     b64str  = base64.b64encode(buffer_)

>>> response = requests.post('https://digdet.herokuapp.com/api/detect', { "image": b64str })
>>> if response.ok:
...     text = response.text
...     res  = json.loads(text)
...     
...     pprint.pprint(res)
... else:
        response.raise_for_status()
```

You'd then recieve a response as follows:

```python
{'data': [{'digit': 2,
           'rect': {'height': 191, 'width': 141, 'x': 236, 'y': 102}},
          {'digit': 8, 'rect': {'height': 214, 'width': 107, 'x': 29, 'y': 94}},
          {'digit': 0,
           'rect': {'height': 181, 'width': 152, 'x': 461, 'y': 60}}],
 'id': '4ce7f21166144ddfaf9746fcbec3ff5a',
 'status': 'success',
 'version': '0.1.0'}
>>>
```

A generic successful response is of the following format:

```json
{
    "id": "<unique_response_id>",
    "version": "<api_version>",
    "status": "success",
    "data":
    [
      {
        "digit": "<recognized_digit>",
        "rect":
        {
          "x": "<x_coordinate>",
          "y": "<y_coordinate>",
          "width": "<contour_width>",
          "height": "<contour_height>"
        }
      }
    ]
}
```

### Dependencies
* Python 2.7 and more or 3.5 and more
* Node.js
* SASS

### License
This repository has been released under the [MIT License](LICENSE).
