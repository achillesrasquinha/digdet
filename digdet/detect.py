# imports - third-party imports
import numpy as np
import cv2

# imports - compatibility imports
from digdet.config.app import AppConfig
from digdet.util import get_cv_version, autodict, area_rect

import digdet

def detect(image, glyph = AppConfig.DEFAULT_GLYPH):
    array       = np.asarray(image, dtype = np.uint8)
    array       = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    gray        = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)

    blur        = cv2.GaussianBlur(gray, **AppConfig.Parameters.GAUSSIAN_BLUR)

    _, thresh   = cv2.threshold(blur, **AppConfig.Parameters.THRESHOLD)
    threshcpy   = thresh.copy()

    version     = get_cv_version()

    if version.major == 3:
        _, contours, _ = cv2.findContours(threshcpy, **AppConfig.Parameters.FIND_CONTOURS)
    else:
        _, contours    = cv2.findContours(threshcpy, **AppConfig.Parameters.FIND_CONTOURS)

    rects       = [cv2.boundingRect(contour) for contour in contours]
    area_image  = gray.size
    area_thresh = 0.01

    rects       = [rect for rect in rects if (area_rect(rect) / area_image) >= area_thresh]

    model       = digdet.load(digdet.MNIST)

    regions     = [ ]

    scale       = 1.5

    for i, rect in enumerate(rects):
        x, y, w, h    = rect
        data          = autodict()

        data['rect']  = { "x": x, "y": y, "width": w, "height": h }

        width, height = int(w * scale), int(h * scale)
        a, b          = max(0, int(x + w / 2 - width  / 2)), max(0, int(y + h / 2 - height / 2))

        region        = thresh[ b : b + height , a : a + width ]
        region        = cv2.resize(region, AppConfig.MNIST_SIZE_INPUT, interpolation = cv2.INTER_AREA)
        region        = cv2.dilate(region, (3, 3))

        row           = region.flatten()
        norm          = row / 255
        features      = np.atleast_2d(norm)
        output        = model.predict(features)
        label         = np.argmax(output)

        digit         = int(label)

        data['digit'] = digit

        regions.append(data)

    return regions
