![](../.github/logo.png)
> A realtime digit OCR on the browser using Machine Learning

# API
> Version - 0.2.0

### Detection
#### General
| Key    | Value                                   |
|--------|-----------------------------------------|
| URL    | https://digdet.herokuapp.com/api/detect |
| Method | POST                                    |

#### Parameters
| Name    | Type                      | Description                                   | Required |
|---------|---------------------------|-----------------------------------------------|----------|
| `image` | `String`                  | base-64 encoded binary data of the image.     | Yes      |
| `lang`  | `Array<String>`           | Glyph Codes, defaults to `["la"]`             | Optional |

#### Returns
| Fields    | Type     | Values                           | Description
|-----------|----------|----------------------------------|------------
| `status`  | `String` | `"success"`, `"fail"`, `"error"` | status of the response.
| `version` | `String` |                                  | api version.
| `id`      | `String` | UUID string                      | unique UUID string for each response
| `data`    | `Array`  |                                  | an array of detected digits.

#### Example
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
```

### Supported Glyphs
#### General
| Key    | Value                                   |
|--------|-----------------------------------------|
| URL    | https://digdet.herokuapp.com/api/glyph  |

#### Returns
An array of supported glyphs of the structure:
```json
[
  {
    "code": "<glyph code>",
    "script": "<script name>",
    "numeral": [
      "<numeral name 1>",
      "<numeral name 2>",
      "<numeral name n>",
    ]
  },
  {
    "code": "...",
  }
]
```

#### Available Glyphs
| Code | Script | Numeral
|------|--------|---------
| la   | Latin  | Arabic, Hindu, Hindu-Arabic
