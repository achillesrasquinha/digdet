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
Send in a base-64 encoded image string HTTP POST (with `image` as the parameter) request to [https://digdet.herokuapp.com/api/detect](https://digdet.herokuapp.com/api/detect). You'd then recieve a sample response as follows:
```json
{
    "id": "<unique_response_id>",
    "version": "<api_version>",
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
