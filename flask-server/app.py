from flask import Flask, request, render_template
from flask_cors import CORS
from flask import jsonify
from pathlib import Path
import base64
import drawBot
from flask import current_app, jsonify, request


base = Path(__file__).parent

app = Flask(__name__)
CORS(app)  # important because the requests are made from outside of flask "cross origin"


@app.route("/test_0", methods=["GET", "POST"], strict_slashes=False)
def get_data():
    title = request.json.get('title', "Hello")
    fontSize = request.json.get('fontSize', 20)
    if title:
        message = f"This is the {title} and this is the {fontSize}"
    else:
        message = "No data found"

    txt = f"{title}"
    drawBot.newDrawing()
    FRAMES = 25
    FRAMES_MOVE = 10
    FRAMEPAUSE = 5

    CANVASW = 800
    CANVASH = 800

    newList = list(txt)
    FONTSIZE = 200
    FONT = "SF-Mono-Semibold.otf"
    fontSettings = {"fontSize": FONTSIZE}

    SPLITLETTER = True
    DOUBLESPLIT = False
    PAUSE = True
    if SPLITLETTER == True:
        PAUSE == False

    XX = 0
    XX_1 = XX
    XX_2 = XX
    MOVE_X = 40
    MOVE_X_STEP = (MOVE_X/FRAMES_MOVE)
    Y1 = CANVASH/2

    # stroke
    STROKEWIDTH = 1
    STROKEWIDTH_2 = 1.5
    # background-color
    rBC = 241/255
    gBC = 241/255
    bBC = 241/255
    # Color1
    rBC2 = 168/255
    gBC2 = 191/255
    bBC2 = 171/255
    # Color2
    rBC3 = 61/255
    gBC3 = 52/255
    bBC3 = 228/255
    # Color3
    rBC1 = 188/255
    gBC1 = 238/255
    bBC1 = 52/255
    # Color4
    rBC4 = 252/255
    gBC4 = 113/255
    bBC4 = 214/255
    # strokewidth special
    if rBC == rBC1 and gBC == gBC1 and bBC == bBC1:
        STROKEWIDTH_2 = 2
    if rBC == rBC2 and gBC == gBC2 and bBC == bBC2:
        STROKEWIDTH_2 = 2

    # height & width
    path = drawBot.BezierPath()
    path.text(txt, (XX, Y1), font=FONT, fontSize=FONTSIZE)
    minx, miny, maxx, maxy = path.bounds()
    h = (maxy-miny) * 1
    H = h
    H1 = 0
    H2 = H

    STEP = H/FRAMES

    # for centering text
    path = drawBot.BezierPath()
    path.text(txt, (0, 0), font=FONT, fontSize=FONTSIZE)
    left, bottom, right, top = path.bounds()
    length = right - left
    heightText = top-bottom
    pathTest = drawBot.BezierPath()
    pathTest.text("P", (XX, Y1), font=FONT, fontSize=FONTSIZE)
    minx, miny, maxx, maxy = pathTest.bounds()
    wTest = maxx - minx
    CENTER = wTest*0.5+(CANVASW-length)/2
    YY = CANVASH/2 - heightText/2

    def drawLetter(letter, number, blendModeX, XX,  H=H, rBC1=rBC1, gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH):
        if letter != ' ':
            path = drawBot.BezierPath()
            path.text(letter, (XX, YY), font=FONT,
                      fontSize=fontSettings["fontSize"], align="center")
            minx, miny, maxx, maxy = path.bounds()

            w = (maxx-minx) * 0.5

            if number == 1:
                bottomLeft = drawBot.BezierPath()
                if blendModeX == 1:
                    drawBot.blendMode("normal")
                if drawBot.blendMode == 0:
                    blendModeX("normal")
                drawBot.fill(rBC1, gBC1, bBC1)
                bottomLeft.rect(minx, miny, w, H)
            elif number == 0:
                bottomLeft = drawBot.BezierPath()
                drawBot.fill(rBC1, gBC1, bBC1)
                bottomLeft.rect(minx+w, miny, w, H)

            drawBot.stroke(rBC1, gBC1, bBC1)
            drawBot.strokeWidth(STROKEWIDTH)
            bottomLeft = bottomLeft & path
            drawBot.drawPath(bottomLeft)

    XX = 0
    #  #fill letter
    H1 = 0
    helpVar = 0
    for frame in range(FRAMES):
        drawBot.newPage(CANVASW, CANVASH)
        drawBot.fill(rBC, gBC, bBC)
        drawBot.rect(0, 0, CANVASW, CANVASH)
        drawBot.frameDuration(1 / 24)
        drawBot.fontSize(fontSettings["fontSize"])
        drawBot.font(FONT)
        drawBot.translate(CENTER, 0)
        for letter in newList:

            if H1 <= H:
                letterWidth, letterHeight = drawBot.textSize(letter)
                drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC4,
                           gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH)
                drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC1,
                           gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=0)
                drawLetter(letter, 1, 0, XX=XX, H=H1, rBC1=rBC2,
                           gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH_2)
                drawLetter(letter, 0, 0, XX=XX, H=H2, rBC1=rBC3,
                           gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH_2)
                helpVar += 1

            if helpVar < len(newList):
                H1 = H1
                H2 = H2
            else:
                H1 += STEP
                H2 -= STEP
            drawBot.translate(letterWidth, 0)

        helpVar = 0
    # print(installedFonts())

    H1 = 0
    H2 = h

    if PAUSE == True:
        for frame in range(FRAMEPAUSE):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:

                if H1 <= H:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                drawBot.translate(letterWidth, 0)

    helpVar = 0
    # move Letter out
    if SPLITLETTER == True:
        for frame in range(FRAMES_MOVE):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:
                letterWidth, letterHeight = drawBot.textSize(letter)
                if XX_1 >= XX - MOVE_X:
                    drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                    helpVar += 1
                    # print(helpVar)

                if helpVar < len(newList):
                    XX_1 = XX_1
                    XX_2 = XX_2
                else:
                    XX_1 -= MOVE_X_STEP
                    XX_2 += MOVE_X_STEP

                drawBot.translate(letterWidth, 0)
            helpVar = 0

    XX_1 = XX - MOVE_X
    XX_2 = XX + MOVE_X
    helpVar = 0
    # move Letter in
    if SPLITLETTER == True:
        for frame in range(FRAMES_MOVE):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:
                letterWidth, letterHeight = drawBot.textSize(letter)
                if XX_1 >= XX - MOVE_X:
                    drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                    helpVar += 1
                    # print(helpVar)

                if helpVar < len(newList):
                    XX_1 = XX_1
                    XX_2 = XX_2
                else:
                    XX_1 += MOVE_X_STEP
                    XX_2 -= MOVE_X_STEP

                drawBot.translate(letterWidth, 0)
            helpVar = 0

    # Doublesplit
    if DOUBLESPLIT == True:
        if SPLITLETTER == True:
            for frame in range(FRAMES_MOVE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    if XX_1 >= XX - MOVE_X:
                        drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC,
                                   gBC1=gBC, bBC1=bBC, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                        helpVar += 1
                        # print(helpVar)

                    if helpVar < len(newList):
                        XX_1 = XX_1
                        XX_2 = XX_2
                    else:
                        XX_1 -= MOVE_X_STEP
                        XX_2 += MOVE_X_STEP

                    drawBot.translate(letterWidth, 0)
                helpVar = 0

        XX_1 = XX - MOVE_X
        XX_2 = XX + MOVE_X
        helpVar = 0
        # move Letter in
        if SPLITLETTER == True:
            for frame in range(FRAMES_MOVE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    if XX_1 >= XX - MOVE_X:
                        drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC,
                                   gBC1=gBC, bBC1=bBC, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                        helpVar += 1
                        # print(helpVar)

                    if helpVar < len(newList):
                        XX_1 = XX_1
                        XX_2 = XX_2
                    else:
                        XX_1 += MOVE_X_STEP
                        XX_2 -= MOVE_X_STEP

                    drawBot.translate(letterWidth, 0)
                helpVar = 0

    # #fill letter
    H1 = 0
    H2 = h
    helpVar = 0

    for frame in range(FRAMES):
        drawBot.newPage(CANVASW, CANVASH)
        drawBot.fill(rBC, gBC, bBC)
        drawBot.rect(0, 0, CANVASW, CANVASH)
        drawBot.frameDuration(1 / 24)
        drawBot.fontSize(fontSettings["fontSize"])
        drawBot.font(FONT)
        drawBot.translate(CENTER, 0)
        for letter in newList:

            if H1 <= H:
                letterWidth, letterHeight = drawBot.textSize(letter)
                drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC2,
                           gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC3,
                           gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH)
                drawLetter(letter, 1, 0, XX=XX, H=H1, rBC1=rBC4,
                           gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH_2)
                helpVar += 1
                drawLetter(letter, 0, 0, XX=XX, H=H2, rBC1=rBC1,
                           gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH_2)
            if helpVar < len(newList):
                H1 = H1
                H2 = H2
            else:
                H1 += STEP
                H2 -= STEP
            drawBot.translate(letterWidth, 0)
        helpVar = 0

    H1 = 0
    H2 = h
    if PAUSE == True:
        for frame in range(FRAMEPAUSE):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:

                if H1 <= H:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC4,
                               gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC3,
                               gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH)
                drawBot.translate(letterWidth, 0)

            drawBot.saveImage("giddyup.gif")
            drawBot.endDrawing()
    with open(base/"giddyup.gif", "rb") as input_file:
        image_string = base64.b64encode(
            input_file.read()).decode('ascii')

    return {"message": message, "image_string": image_string}, 200


""" @app.route("/test_0", methods=["GET", "POST"], strict_slashes=False)
def get_data():
    title = request.json.get('title', "Hello")
    fontSize = request.json.get('fontSize', 20)
    if title:
        message = f"This is the {title} and this is the {fontSize}"
    else:
        message = "No data found"

    return {"message": message}, 200    """


@app.route('/test', methods=["GET", "POST"])
def mes():
    form = request.form
    nickname = form.get("nickname")
    if nickname:
        message = f"Hello {nickname}"
    else:
        message = "No nickname provided"
    return render_template("test_2_form.html", message=message)


@app.route('/test_2', methods=["GET", "POST"])
def hello_2():
    image_string = None
    message = None
    if request.method == "POST":
        form = request.form
        nickname = form.get("nickname")
        if nickname:
            message = f"Hello {nickname}"
        else:
            message = "No nickname provided"

        txt = f"{nickname}"
        drawBot.newDrawing()
        FRAMES = 25
        FRAMES_MOVE = 10
        FRAMEPAUSE = 5

        CANVASW = 1000
        CANVASH = 1000

        newList = list(txt)
        FONTSIZE = 150
        FONT = "SF-Mono-Semibold.otf"
        fontSettings = {"fontSize": FONTSIZE}

        # for eachFontName in installedFonts():
        #     print(eachFontName)

        SPLITLETTER = True
        DOUBLESPLIT = False
        PAUSE = True
        if SPLITLETTER == True:
            PAUSE == False

        XX = 0
        XX_1 = XX
        XX_2 = XX
        MOVE_X = 40
        MOVE_X_STEP = (MOVE_X/FRAMES_MOVE)
        Y1 = CANVASH/2

        # stroke
        STROKEWIDTH = 1
        STROKEWIDTH_2 = 1.5
        # background-color
        rBC = 241/255
        gBC = 241/255
        bBC = 241/255
        # Color1
        rBC2 = 252/255
        gBC2 = 220/255
        bBC2 = 0/255
        # Color2
        rBC3 = 0/255
        gBC3 = 156/255
        bBC3 = 224/255
        # Color3
        rBC1 = 253/255
        gBC1 = 161/255
        bBC1 = 255/255
        # Color4
        rBC4 = 219/255
        gBC4 = 223/255
        bBC4 = 0/255
        # strokewidth special
        if rBC == rBC1 and gBC == gBC1 and bBC == bBC1:
            STROKEWIDTH_2 = 2
        if rBC == rBC2 and gBC == gBC2 and bBC == bBC2:
            STROKEWIDTH_2 = 2

        # height & width
        path = drawBot.BezierPath()
        path.text(txt, (XX, Y1), font=FONT, fontSize=FONTSIZE)
        minx, miny, maxx, maxy = path.bounds()
        h = (maxy-miny) * 1
        H = h
        H1 = 0
        H2 = H

        STEP = H/FRAMES

        # for centering text
        path = drawBot.BezierPath()
        path.text(txt, (0, 0), font=FONT, fontSize=FONTSIZE)
        left, bottom, right, top = path.bounds()
        length = right - left
        heightText = top-bottom
        pathTest = drawBot.BezierPath()
        pathTest.text("P", (XX, Y1), font=FONT, fontSize=FONTSIZE)
        minx, miny, maxx, maxy = pathTest.bounds()
        wTest = maxx - minx
        CENTER = wTest*0.5+(CANVASW-length)/2
        YY = CANVASH/2 - heightText/2

        def drawLetter(letter, number, blendModeX, XX,  H=H, rBC1=rBC1, gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH):
            if letter != ' ':
                path = drawBot.BezierPath()
                path.text(letter, (XX, YY), font=FONT,
                          fontSize=fontSettings["fontSize"], align="center")
                minx, miny, maxx, maxy = path.bounds()

                w = (maxx-minx) * 0.5

                if number == 1:
                    bottomLeft = drawBot.BezierPath()
                    if blendModeX == 1:
                        drawBot.blendMode("normal")
                    if drawBot.blendMode == 0:
                        blendModeX("normal")
                    drawBot.fill(rBC1, gBC1, bBC1)
                    bottomLeft.rect(minx, miny, w, H)
                elif number == 0:
                    bottomLeft = drawBot.BezierPath()
                    drawBot.fill(rBC1, gBC1, bBC1)
                    bottomLeft.rect(minx+w, miny, w, H)

                drawBot.stroke(rBC1, gBC1, bBC1)
                drawBot.strokeWidth(STROKEWIDTH)
                bottomLeft = bottomLeft & path
                drawBot.drawPath(bottomLeft)

        XX = 0
        #  #fill letter
        H1 = 0
        helpVar = 0
        for frame in range(FRAMES):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:

                if H1 <= H:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC4,
                               gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=0)
                    drawLetter(letter, 1, 0, XX=XX, H=H1, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH_2)
                    drawLetter(letter, 0, 0, XX=XX, H=H2, rBC1=rBC3,
                               gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH_2)
                    helpVar += 1

                if helpVar < len(newList):
                    H1 = H1
                    H2 = H2
                else:
                    H1 += STEP
                    H2 -= STEP
                drawBot.translate(letterWidth, 0)

            helpVar = 0
        # print(installedFonts())

        H1 = 0
        H2 = h

        if PAUSE == True:
            for frame in range(FRAMEPAUSE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:

                    if H1 <= H:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC2,
                                   gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                    drawBot.translate(letterWidth, 0)

        helpVar = 0
        # move Letter out
        if SPLITLETTER == True:
            for frame in range(FRAMES_MOVE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    if XX_1 >= XX - MOVE_X:
                        drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC2,
                                   gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                        helpVar += 1
                        # print(helpVar)

                    if helpVar < len(newList):
                        XX_1 = XX_1
                        XX_2 = XX_2
                    else:
                        XX_1 -= MOVE_X_STEP
                        XX_2 += MOVE_X_STEP

                    drawBot.translate(letterWidth, 0)
                helpVar = 0

        XX_1 = XX - MOVE_X
        XX_2 = XX + MOVE_X
        helpVar = 0
        # move Letter in
        if SPLITLETTER == True:
            for frame in range(FRAMES_MOVE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    if XX_1 >= XX - MOVE_X:
                        drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC2,
                                   gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                        helpVar += 1
                        # print(helpVar)

                    if helpVar < len(newList):
                        XX_1 = XX_1
                        XX_2 = XX_2
                    else:
                        XX_1 += MOVE_X_STEP
                        XX_2 -= MOVE_X_STEP

                    drawBot.translate(letterWidth, 0)
                helpVar = 0

        # Doublesplit
        if DOUBLESPLIT == True:
            if SPLITLETTER == True:
                for frame in range(FRAMES_MOVE):
                    drawBot.newPage(CANVASW, CANVASH)
                    drawBot.fill(rBC, gBC, bBC)
                    drawBot.rect(0, 0, CANVASW, CANVASH)
                    drawBot.frameDuration(1 / 24)
                    drawBot.fontSize(fontSettings["fontSize"])
                    drawBot.font(FONT)
                    drawBot.translate(CENTER, 0)
                    for letter in newList:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        if XX_1 >= XX - MOVE_X:
                            drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC,
                                       gBC1=gBC, bBC1=bBC, STROKEWIDTH=STROKEWIDTH)
                            drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                       gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                            helpVar += 1
                            # print(helpVar)

                        if helpVar < len(newList):
                            XX_1 = XX_1
                            XX_2 = XX_2
                        else:
                            XX_1 -= MOVE_X_STEP
                            XX_2 += MOVE_X_STEP

                        drawBot.translate(letterWidth, 0)
                    helpVar = 0

            XX_1 = XX - MOVE_X
            XX_2 = XX + MOVE_X
            helpVar = 0
            # move Letter in
            if SPLITLETTER == True:
                for frame in range(FRAMES_MOVE):
                    drawBot.newPage(CANVASW, CANVASH)
                    drawBot.fill(rBC, gBC, bBC)
                    drawBot.rect(0, 0, CANVASW, CANVASH)
                    drawBot.frameDuration(1 / 24)
                    drawBot.fontSize(fontSettings["fontSize"])
                    drawBot.font(FONT)
                    drawBot.translate(CENTER, 0)
                    for letter in newList:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        if XX_1 >= XX - MOVE_X:
                            drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC,
                                       gBC1=gBC, bBC1=bBC, STROKEWIDTH=STROKEWIDTH)
                            drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                       gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                            helpVar += 1
                            # print(helpVar)

                        if helpVar < len(newList):
                            XX_1 = XX_1
                            XX_2 = XX_2
                        else:
                            XX_1 += MOVE_X_STEP
                            XX_2 -= MOVE_X_STEP

                        drawBot.translate(letterWidth, 0)
                    helpVar = 0

        # #fill letter
        H1 = 0
        H2 = h
        helpVar = 0

        for frame in range(FRAMES):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:

                if H1 <= H:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC3,
                               gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 1, 0, XX=XX, H=H1, rBC1=rBC4,
                               gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH_2)
                    helpVar += 1
                    drawLetter(letter, 0, 0, XX=XX, H=H2, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH_2)
                if helpVar < len(newList):
                    H1 = H1
                    H2 = H2
                else:
                    H1 += STEP
                    H2 -= STEP
                drawBot.translate(letterWidth, 0)
            helpVar = 0

        H1 = 0
        H2 = h
        if PAUSE == True:
            for frame in range(FRAMEPAUSE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:

                    if H1 <= H:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC4,
                                   gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC3,
                                   gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH)
                    drawBot.translate(letterWidth, 0)

                drawBot.saveImage("giddyup.gif")
                drawBot.endDrawing()
                with open(base/"giddyup.gif", "rb") as input_file:
                    image_string = base64.b64encode(
                        input_file.read()).decode('ascii')
    return render_template("test_2.html", image_string=image_string, message=message)

#
#
#
#
#
#


@app.route('/test_3', methods=["GET", "POST"])
def hello_3():
    image_string = None
    message = None
    if request.method == "POST":
        form = request.form
        nickname = form.get("nickname")
        if nickname:
            message = f"Hello {nickname}"
        else:
            message = "No nickname provided"

        txt = f"{nickname}"
        drawBot.newDrawing()
        FRAMES = 25
        FRAMES_MOVE = 10
        FRAMEPAUSE = 5

        CANVASW = 800
        CANVASH = 800

        newList = list(txt)
        FONTSIZE = 300
        FONT = "SF-Mono-Semibold.otf"
        fontSettings = {"fontSize": FONTSIZE}

        # for eachFontName in installedFonts():
        #     print(eachFontName)

        SPLITLETTER = True
        DOUBLESPLIT = False
        PAUSE = True
        if SPLITLETTER == True:
            PAUSE == False

        XX = 0
        XX_1 = XX
        XX_2 = XX
        MOVE_X = 40
        MOVE_X_STEP = (MOVE_X/FRAMES_MOVE)
        Y1 = CANVASH/2

        # stroke
        STROKEWIDTH = 1
        STROKEWIDTH_2 = 1.5
        # background-color
        rBC = 241/255
        gBC = 241/255
        bBC = 241/255
        # Color1
        rBC2 = 168/255
        gBC2 = 191/255
        bBC2 = 171/255
        # Color2
        rBC3 = 61/255
        gBC3 = 52/255
        bBC3 = 228/255
        # Color3
        rBC1 = 188/255
        gBC1 = 238/255
        bBC1 = 52/255
        # Color4
        rBC4 = 252/255
        gBC4 = 113/255
        bBC4 = 214/255
        # strokewidth special
        if rBC == rBC1 and gBC == gBC1 and bBC == bBC1:
            STROKEWIDTH_2 = 2
        if rBC == rBC2 and gBC == gBC2 and bBC == bBC2:
            STROKEWIDTH_2 = 2

        # height & width
        path = drawBot.BezierPath()
        path.text(txt, (XX, Y1), font=FONT, fontSize=FONTSIZE)
        minx, miny, maxx, maxy = path.bounds()
        h = (maxy-miny) * 1
        H = h
        H1 = 0
        H2 = H

        STEP = H/FRAMES

        # for centering text
        path = drawBot.BezierPath()
        path.text(txt, (0, 0), font=FONT, fontSize=FONTSIZE)
        left, bottom, right, top = path.bounds()
        length = right - left
        heightText = top-bottom
        pathTest = drawBot.BezierPath()
        pathTest.text("P", (XX, Y1), font=FONT, fontSize=FONTSIZE)
        minx, miny, maxx, maxy = pathTest.bounds()
        wTest = maxx - minx
        CENTER = wTest*0.5+(CANVASW-length)/2
        YY = CANVASH/2 - heightText/2

        def drawLetter(letter, number, blendModeX, XX,  H=H, rBC1=rBC1, gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH):
            if letter != ' ':
                path = drawBot.BezierPath()
                path.text(letter, (XX, YY), font=FONT,
                          fontSize=fontSettings["fontSize"], align="center")
                minx, miny, maxx, maxy = path.bounds()

                w = (maxx-minx) * 0.5

                if number == 1:
                    bottomLeft = drawBot.BezierPath()
                    if blendModeX == 1:
                        drawBot.blendMode("normal")
                    if drawBot.blendMode == 0:
                        blendModeX("normal")
                    drawBot.fill(rBC1, gBC1, bBC1)
                    bottomLeft.rect(minx, miny, w, H)
                elif number == 0:
                    bottomLeft = drawBot.BezierPath()
                    drawBot.fill(rBC1, gBC1, bBC1)
                    bottomLeft.rect(minx+w, miny, w, H)

                drawBot.stroke(rBC1, gBC1, bBC1)
                drawBot.strokeWidth(STROKEWIDTH)
                bottomLeft = bottomLeft & path
                drawBot.drawPath(bottomLeft)

        XX = 0
        #  #fill letter
        H1 = 0
        helpVar = 0
        for frame in range(FRAMES):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:

                if H1 <= H:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC4,
                               gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=0)
                    drawLetter(letter, 1, 0, XX=XX, H=H1, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH_2)
                    drawLetter(letter, 0, 0, XX=XX, H=H2, rBC1=rBC3,
                               gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH_2)
                    helpVar += 1

                if helpVar < len(newList):
                    H1 = H1
                    H2 = H2
                else:
                    H1 += STEP
                    H2 -= STEP
                drawBot.translate(letterWidth, 0)

            helpVar = 0
        # print(installedFonts())

        H1 = 0
        H2 = h

        if PAUSE == True:
            for frame in range(FRAMEPAUSE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:

                    if H1 <= H:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC2,
                                   gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                    drawBot.translate(letterWidth, 0)

        helpVar = 0
        # move Letter out
        if SPLITLETTER == True:
            for frame in range(FRAMES_MOVE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    if XX_1 >= XX - MOVE_X:
                        drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC2,
                                   gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                        helpVar += 1
                        # print(helpVar)

                    if helpVar < len(newList):
                        XX_1 = XX_1
                        XX_2 = XX_2
                    else:
                        XX_1 -= MOVE_X_STEP
                        XX_2 += MOVE_X_STEP

                    drawBot.translate(letterWidth, 0)
                helpVar = 0

        XX_1 = XX - MOVE_X
        XX_2 = XX + MOVE_X
        helpVar = 0
        # move Letter in
        if SPLITLETTER == True:
            for frame in range(FRAMES_MOVE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    if XX_1 >= XX - MOVE_X:
                        drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC2,
                                   gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                   gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                        helpVar += 1
                        # print(helpVar)

                    if helpVar < len(newList):
                        XX_1 = XX_1
                        XX_2 = XX_2
                    else:
                        XX_1 += MOVE_X_STEP
                        XX_2 -= MOVE_X_STEP

                    drawBot.translate(letterWidth, 0)
                helpVar = 0

        # Doublesplit
        if DOUBLESPLIT == True:
            if SPLITLETTER == True:
                for frame in range(FRAMES_MOVE):
                    drawBot.newPage(CANVASW, CANVASH)
                    drawBot.fill(rBC, gBC, bBC)
                    drawBot.rect(0, 0, CANVASW, CANVASH)
                    drawBot.frameDuration(1 / 24)
                    drawBot.fontSize(fontSettings["fontSize"])
                    drawBot.font(FONT)
                    drawBot.translate(CENTER, 0)
                    for letter in newList:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        if XX_1 >= XX - MOVE_X:
                            drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC,
                                       gBC1=gBC, bBC1=bBC, STROKEWIDTH=STROKEWIDTH)
                            drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                       gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                            helpVar += 1
                            # print(helpVar)

                        if helpVar < len(newList):
                            XX_1 = XX_1
                            XX_2 = XX_2
                        else:
                            XX_1 -= MOVE_X_STEP
                            XX_2 += MOVE_X_STEP

                        drawBot.translate(letterWidth, 0)
                    helpVar = 0

            XX_1 = XX - MOVE_X
            XX_2 = XX + MOVE_X
            helpVar = 0
            # move Letter in
            if SPLITLETTER == True:
                for frame in range(FRAMES_MOVE):
                    drawBot.newPage(CANVASW, CANVASH)
                    drawBot.fill(rBC, gBC, bBC)
                    drawBot.rect(0, 0, CANVASW, CANVASH)
                    drawBot.frameDuration(1 / 24)
                    drawBot.fontSize(fontSettings["fontSize"])
                    drawBot.font(FONT)
                    drawBot.translate(CENTER, 0)
                    for letter in newList:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        if XX_1 >= XX - MOVE_X:
                            drawLetter(letter, 1, 1, XX=XX_1, H=h, rBC1=rBC,
                                       gBC1=gBC, bBC1=bBC, STROKEWIDTH=STROKEWIDTH)
                            drawLetter(letter, 0, 1, XX=XX_2, H=h, rBC1=rBC1,
                                       gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH)
                            helpVar += 1
                            # print(helpVar)

                        if helpVar < len(newList):
                            XX_1 = XX_1
                            XX_2 = XX_2
                        else:
                            XX_1 += MOVE_X_STEP
                            XX_2 -= MOVE_X_STEP

                        drawBot.translate(letterWidth, 0)
                    helpVar = 0

        # #fill letter
        H1 = 0
        H2 = h
        helpVar = 0

        for frame in range(FRAMES):
            drawBot.newPage(CANVASW, CANVASH)
            drawBot.fill(rBC, gBC, bBC)
            drawBot.rect(0, 0, CANVASW, CANVASH)
            drawBot.frameDuration(1 / 24)
            drawBot.fontSize(fontSettings["fontSize"])
            drawBot.font(FONT)
            drawBot.translate(CENTER, 0)
            for letter in newList:

                if H1 <= H:
                    letterWidth, letterHeight = drawBot.textSize(letter)
                    drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC2,
                               gBC1=gBC2, bBC1=bBC2, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC3,
                               gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH)
                    drawLetter(letter, 1, 0, XX=XX, H=H1, rBC1=rBC4,
                               gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH_2)
                    helpVar += 1
                    drawLetter(letter, 0, 0, XX=XX, H=H2, rBC1=rBC1,
                               gBC1=gBC1, bBC1=bBC1, STROKEWIDTH=STROKEWIDTH_2)
                if helpVar < len(newList):
                    H1 = H1
                    H2 = H2
                else:
                    H1 += STEP
                    H2 -= STEP
                drawBot.translate(letterWidth, 0)
            helpVar = 0

        H1 = 0
        H2 = h
        if PAUSE == True:
            for frame in range(FRAMEPAUSE):
                drawBot.newPage(CANVASW, CANVASH)
                drawBot.fill(rBC, gBC, bBC)
                drawBot.rect(0, 0, CANVASW, CANVASH)
                drawBot.frameDuration(1 / 24)
                drawBot.fontSize(fontSettings["fontSize"])
                drawBot.font(FONT)
                drawBot.translate(CENTER, 0)
                for letter in newList:

                    if H1 <= H:
                        letterWidth, letterHeight = drawBot.textSize(letter)
                        drawLetter(letter, 1, 0, XX=XX, H=h, rBC1=rBC4,
                                   gBC1=gBC4, bBC1=bBC4, STROKEWIDTH=STROKEWIDTH)
                        drawLetter(letter, 0, 0, XX=XX, H=h, rBC1=rBC3,
                                   gBC1=gBC3, bBC1=bBC3, STROKEWIDTH=STROKEWIDTH)
                    drawBot.translate(letterWidth, 0)

                drawBot.saveImage("giddyup.gif")
                drawBot.endDrawing()
    with open(base/"giddyup.gif", "rb") as input_file:
        image_string = base64.b64encode(
            input_file.read()).decode('ascii')

    return {"image_string": image_string}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
