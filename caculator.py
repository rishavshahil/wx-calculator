from wx import *

app = App()
frame = Frame(None, title='Calculator', size=(400,600))
panel = Panel(frame)

main = BoxSizer(VERTICAL)
panel.SetBackgroundColour('#737373')
screen = TextCtrl(panel)
font1 = Font(50, FONTFAMILY_DECORATIVE, FONTSTYLE_NORMAL, FONTWEIGHT_EXTRABOLD)
screen.SetFont(font1)
screen.SetBackgroundColour('#000000')
screen.SetForegroundColour('white')
main.Add(screen, 1, EXPAND|ALL, border=10 )

# Function
displayData = '0'
screen.SetValue(displayData)
allData = ''


def one_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '1'
    else:
        displayData += '1'
    allData += '1'
    screen.SetValue(displayData)

def two_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '2'
    else:
        displayData += '2'
    allData += '2'
    screen.SetValue(displayData)

def three_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '3'
    else:
        displayData += '3'
    allData += '3'
    screen.SetValue(displayData)

def four_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '4'
    else:
        displayData += '4'
    allData += '4'
    screen.SetValue(displayData)

def five_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '5'
    else:
        displayData += '5'
    allData += '5'
    screen.SetValue(displayData)

def six_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '6'
    else:
        displayData += '6'
    allData += '6'
    screen.SetValue(displayData)

def seven_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '7'
    else:
        displayData += '7'
    allData += '7'
    screen.SetValue(displayData)

def eight_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '8'
    else:
        displayData += '8'
    allData += '8'
    screen.SetValue(displayData)

def nine_fun(event):
    global displayData, allData
    if displayData == '0':
        displayData = '9'
    else:
        displayData += '9'
    allData += '9'
    screen.SetValue(displayData)

def zero_fun(event):
    global displayData, allData
    if displayData != '0':
        displayData += '0'
        screen.SetValue(displayData)
    allData += '0'

def clear_fun(event):
    global displayData, allData
    displayData  = '0'
    allData = ''
    screen.SetValue(displayData)

def back_fun(event):
    global displayData, allData
    if len(displayData) == 1:
        displayData = '0'
        allData = ''
    else:
        displayData = displayData[:len(displayData)-1:]
        allData = displayData
    screen.SetValue(displayData)

def add_fun(event):
    global displayData, allData
    if displayData == '0':
        allData = '+'
    else:
        allData += '+'
    displayData = '0'
    screen.SetValue(displayData)

def subtract_fun(event):
    global displayData, allData
    if displayData == '0':
        allData = '-'
    else:
        allData += '-'
    displayData = '0'
    screen.SetValue(displayData)

def multiply_fun(event):
    global displayData, allData
    if displayData == '0':
        allData = '*'
    else:
        allData += '*'
    displayData = '0'
    screen.SetValue(displayData)

def divide_fun(event):
    global displayData, allData
    if displayData == '0':
        allData = '/'
    else:
        allData += '/'
    displayData = '0'
    screen.SetValue(displayData)

def equalTo_fun(event):
    global displayData, allData
    if allData:
        displayData = str(eval(allData))
        allData = displayData
    screen.SetValue(displayData)

def dot_fun(event):
    global displayData, allData
    displayData += '.'
    allData += '.'
    screen.SetValue(displayData)

def plusMinus_fun(event):
    global displayData, allData
    if eval(displayData) > 0:
        displayData = str(-1*eval(displayData))
    else:
        displayData = str(-1*eval(displayData))
    screen.SetValue(displayData)

btnGroup = GridSizer(5,4,5,5)
# Button Start
one = Button(panel, label="1")
two = Button(panel, label="2")
three = Button(panel, label="3")
four = Button(panel, label="4")
five = Button(panel, label="5")
six = Button(panel, label="6")
seven = Button(panel, label="7")
eight = Button(panel, label="8")
nine = Button(panel, label="9")
zero = Button(panel, label="0")
dot = Button(panel, label=".")
add = Button(panel, label="+")
subtract = Button(panel, label="-")
multiply = Button(panel, label="X")
divide = Button(panel, label="÷")
back = Button(panel, label="⌫")
percentage = Button(panel, label="%")
clear = Button(panel, label="C")
plusMinus = Button(panel, label="+/-")
equalTo = Button(panel, label="=")

one.SetBackgroundColour('#0d0d0d')
two.SetBackgroundColour('#0d0d0d')
three.SetBackgroundColour('#0d0d0d')
four.SetBackgroundColour('#0d0d0d')
five.SetBackgroundColour('#0d0d0d')
six.SetBackgroundColour('#0d0d0d')
seven.SetBackgroundColour('#0d0d0d')
eight.SetBackgroundColour('#0d0d0d')
nine.SetBackgroundColour('#0d0d0d')
zero.SetBackgroundColour('#0d0d0d')

equalTo.SetBackgroundColour('#ffa500')
add.SetBackgroundColour('#333333')
subtract.SetBackgroundColour('#333333')
multiply.SetBackgroundColour('#333333')
divide.SetBackgroundColour('#333333')
percentage.SetBackgroundColour('#333333')
plusMinus.SetBackgroundColour('#333333')
dot.SetBackgroundColour('#333333')
clear.SetBackgroundColour('#333333')
back.SetBackgroundColour('#333333')

one.SetForegroundColour('white')
two.SetForegroundColour('white')
three.SetForegroundColour('white')
four.SetForegroundColour('white')
five.SetForegroundColour('white')
six.SetForegroundColour('white')
seven.SetForegroundColour('white')
eight.SetForegroundColour('white')
nine.SetForegroundColour('white')
zero.SetForegroundColour('white')

equalTo.SetForegroundColour('black')
add.SetForegroundColour('white')
subtract.SetForegroundColour('white')
multiply.SetForegroundColour('white')
divide.SetForegroundColour('white')
percentage.SetForegroundColour('white')
plusMinus.SetForegroundColour('white')
dot.SetForegroundColour('white')
clear.SetForegroundColour('#ffa500')
back.SetForegroundColour('white')

font2 = Font(30, FONTFAMILY_MODERN, FONTSTYLE_NORMAL, FONTWEIGHT_EXTRABOLD)

one.SetFont(font2)
two.SetFont(font2)
three.SetFont(font2)
four.SetFont(font2)
five.SetFont(font2)
six.SetFont(font2)
seven.SetFont(font2)
eight.SetFont(font2)
nine.SetFont(font2)
zero.SetFont(font2)

equalTo.SetFont(font2)
add.SetFont(font2)
subtract.SetFont(font2)
multiply.SetFont(font2)
divide.SetFont(font2)
percentage.SetFont(font2)
plusMinus.SetFont(font2)
dot.SetFont(font2)
clear.SetFont(font2)
back.SetFont(font2)

#function binding

one.Bind(EVT_BUTTON, one_fun, one)
two.Bind(EVT_BUTTON, two_fun, two)
three.Bind(EVT_BUTTON, three_fun, three)
four.Bind(EVT_BUTTON, four_fun, four)
five.Bind(EVT_BUTTON, five_fun, five)
six.Bind(EVT_BUTTON, six_fun, six)
seven.Bind(EVT_BUTTON, seven_fun, seven)
eight.Bind(EVT_BUTTON, eight_fun, eight)
nine.Bind(EVT_BUTTON, nine_fun, nine)
zero.Bind(EVT_BUTTON, zero_fun, zero)
back.Bind(EVT_BUTTON, back_fun, back)
clear.Bind(EVT_BUTTON, clear_fun, clear)
add.Bind(EVT_BUTTON, add_fun, add)
subtract.Bind(EVT_BUTTON, subtract_fun, subtract)
multiply.Bind(EVT_BUTTON, multiply_fun, multiply)
divide.Bind(EVT_BUTTON, divide_fun, divide)
equalTo.Bind(EVT_BUTTON, equalTo_fun, equalTo)
dot.Bind(EVT_BUTTON, dot_fun, dot)
plusMinus.Bind(EVT_BUTTON, plusMinus_fun, plusMinus)




btnGroup.AddMany([
    (clear, 1, EXPAND),
    (percentage, 1, EXPAND),
    (divide, 1, EXPAND),
    (back, 1, EXPAND),
    (seven, 1, EXPAND),
    (eight, 1, EXPAND),
    (nine, 1, EXPAND),
    (multiply, 1, EXPAND),
    (four, 1, EXPAND),
    (five, 1, EXPAND),
    (six, 1, EXPAND),
    (subtract, 1, EXPAND),
    (one, 1, EXPAND),
    (two, 1, EXPAND),
    (three, 1, EXPAND),
    (add, 1, EXPAND),
    (plusMinus, 1, EXPAND),
    (zero, 1, EXPAND),
    (dot, 1, EXPAND),
    (equalTo, 1, EXPAND),
])


    


main.Add(btnGroup, 4, EXPAND|LEFT|RIGHT|BOTTOM, border=10)

panel.SetSizer(main)
frame.Show()
app.MainLoop()