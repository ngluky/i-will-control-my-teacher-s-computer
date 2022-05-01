import json, pyautogui ,numpy , cv2, random, string , win10toast, logging
from flask import Flask, send_file , request , make_response, Response
from pynput.keyboard import Controller,Key
from pynput.mouse import Button
from pynput.mouse import Controller as Controller_m

import PIL.ImageGrab
 

#pyinstaller --onefile -w .\main.py

# from pyautogui import KEYBOARD_KEYS
toa = win10toast.ToastNotifier()


key_con = Controller()
mou_con = Controller_m()

key_pynput = {
    8: Key.backspace,
    9: Key.alt,
    13: Key.enter,
    16:Key.shift,
    17: Key.ctrl,
    18: Key.alt,
    19: Key.pause,
    20: Key.caps_lock,
    27: Key.esc,
    33:Key.page_up,
    32: Key.space,
    34: Key.page_down,
    35:Key.end,
    36:Key.home,
    37: Key.left,
    38: Key.up,
    39: Key.right,
    40: Key.down,
    44: Key.print_screen,
    45: Key.insert,
    46: Key.delete,
    48:'0',
    49:'1',
    50:'2',
    51:'3',
    52:'4',
    53:'5',
    54:'6',
    55:'7',
    56:'8',
    57:'9',
    65:'a',
    66:'b',
    67:'c',
    68:'d',
    69:'e',
    70:'f',
    71:'g',
    72:'h',
    73:'i',
    74:'j',
    75:'k',
    76:'l',
    77:'m',
    78:'n',
    79:'o',
    80:'p',
    81:'q',
    82:'r',
    83:'s',
    84:'t',
    85:'u',
    86:'v',
    87:'w',
    88:'x',
    89:'y',
    90:'z',
    91:'left window key',
    92:'right window key',
    93:'select key',
    96:'0',
    97:'1',
    98:'2',
    99:'3',
    100:'4',
    101:'5',
    102:'6',
    103:'7',
    104:'8',
    105:'9',
    112: Key.f1,
    113: Key.f2,
    114: Key.f3,
    115: Key.f4,
    116: Key.f5,
    117: Key.f6,
    118: Key.f7,
    119: Key.f8,
    120: Key.f9,
    121: Key.f1,
    122: Key.f1,
    123: Key.f1,
    144: Key.num_lock,
    145: Key.scroll_lock,
}


#pyinstaller --onefile -w .\main.py

# # lấy file tạm
# index = open('html\index.html' , encoding='utf-8')
# index_js = open('html\index.js' , encoding='utf-8')
# loin = open('html\loin.html', encoding='utf-8')
# loin_js = open('html\loin.js', encoding='utf-8')
# files = {
#     "index.html": index.read(),
#     "index.js": index_js.read(),
#     "loin.html": loin.read(),
#     "loin.js": loin_js.read(),
# }
files = {
    "index.html": 
        r'<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <!-- <link rel="stylesheet" href="file/style.css"> --> <style> * { margin: 0; padding: 0; -moz-user-select: none !important; -webkit-touch-callout: none !important; -webkit-user-select: none !important; -khtml-user-select: none !important; -moz-user-select: none !important; -ms-user-select: none !important; user-select: none !important; } body { background-color: rgb(114, 104, 104); height: 100vh; } .main { height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; } .main .camvar { width: 80%; background-color: white; background-repeat: no-repeat; background-size: contain; position: relative; z-index: 1; } .main canvas { position: relative; height: inherit; width: inherit; z-index: 10; position: absolute; left: 0; } .main .chat { margin-top: 10px; /* margin-bottom:; */ } .main #lam_ { position: absolute; height: 100%; width: 100%; left: 0; top:0; z-index: 10 } .main .button { margin-top: 10px; } </style></head><body> <div class="main"> <div class="camvar"> <img src="/strim" width="100%" height="100%"> <canvas></canvas> <!-- <div id="lam_"></div> --> </div> <div class="chat"> <input type="text" id="tile" placeholder="tile"> </div> <div class="chat"> <input type="text" id="mess" placeholder="mess"> <!-- <button onclick="" style="visibility:hidden">send</button> --> </div> <div class="button"> <button onclick="send_()">send</button> <select name="resolution" id="resolution"> <option value="480">480p</option> <option value="720">720p</option> <option value="hd">hd</option> </select> </div> </div> <script src="file/index.js"></script></body></html>',
    "index.js":
        r'const canvas=document.querySelector("canvas"),resolution=document.getElementById("resolution"),size={x:0,y:0};function re16_9(){var e=document.querySelector("canvas"),t=document.querySelector(".main .camvar"),o=9*t.offsetWidth/16,n=t.offsetWidth;t.style.height=`${o}px`,e.style.width=`${n}px`}function size_(){fetch("/size").then(e=>e.json()).then(e=>{size.x=e.x,size.y=e.y})}document.addEventListener("contextmenu",e=>e.preventDefault()),re16_9(),window.addEventListener("resize",e=>{re16_9()}),size_();var mouse_dow=!1;canvas.addEventListener("mousemove",mousemove_);var date=new Date,time_s=date.getTime();function mousemove_(e){if((date=new Date).getTime()-time_s>90&&(time_s=date.getTime(),mouse_dow)){var t=x_y(e),o=t.x,n=t.y;fetch("/mou_api",{method:"POST",body:JSON.stringify({x:o,y:n,type:"move",button:e.button})})}}function x_y(e){var t=e.offsetX,o=e.offsetY;return{x:Math.round(t*size.x/canvas.offsetWidth),y:Math.round(o*size.y/canvas.offsetHeight)}}function send_(){var e=document.getElementById("mess"),t=document.getElementById("tile");console.log(e.value),fetch("/notly",{method:"POST",body:JSON.stringify({title:t.value,message:e.value})}),e.value="",t.value=""}canvas.addEventListener("mousedown",e=>{console.log(e);var t=x_y(e),o=t.x,n=t.y;mouse_dow=!0,fetch("/mou_api",{method:"POST",body:JSON.stringify({x:o,y:n,type:"dow",button:e.button})})}),canvas.addEventListener("wheel",e=>{console.log(e.deltaY);var t=x_y(e),o=t.x,n=t.y;fetch("/mou_api",{method:"POST",body:JSON.stringify({x:o,y:n,type:"wheel",button:0,dY:e.deltaY,dX:e.deltaX})})}),canvas.addEventListener("mouseup",e=>{var t=x_y(e),o=t.x,n=t.y;mouse_dow=!1,fetch("/mou_api",{method:"POST",body:JSON.stringify({x:o,y:n,type:"up",button:e.button})})}),window.onload=function(){document.addEventListener("mousedown",function(e){lastDownTarget=e.target},!1),document.addEventListener("keydown",function(e){lastDownTarget==canvas&&(console.log(e.keyCode),fetch("/key_api",{method:"POST",body:JSON.stringify({key:`${e.keyCode}`,type:"down"})}))},!1),document.addEventListener("keyup",function(e){lastDownTarget==canvas&&(console.log(e.keyCode),fetch("/key_api",{method:"POST",body:JSON.stringify({key:`${e.keyCode}`,type:"up"})}))},!1)},resolution.addEventListener("change",e=>{fetch("/size",{method:"POST",body:JSON.stringify({resolution:resolution.value})})});',
    "loin.html":
        r'<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <!-- <link rel="stylesheet" href="file/loin.css"> --> <style> * { padding:0; margin:0; font-size:20px } body { height:100vh; display:flex; justify-content:center; align-items:center; background-color:#726868 } .main { background-color:#fff; padding:30px; border-radius:10px; display:flex; flex-direction:column } .in { display:flex; justify-content:space-between; margin-top:20px; margin-bottom:20px } </style></head><body> <div class="main"> <div class="in"> <p>name: </p> <input type="text" id="name"> </div> <div class="in"> <p>pass: </p> <input type="password" id="pass"> </div> <button onclick="loin()"> loin </button> <button onclick="guest()"> chế độ khách </button> </div> <script src="file/loin.js"></script></body></html>',
    "loin.js":
        r'const url=window.location.origin;function loin(){var o=document.querySelector("#name"),e=document.querySelector("#pass"),n=o.value,t=e.value;console.log(n),console.log(t),fetch("/api_loin",{method:"POST",body:JSON.stringify({name:n,pass:t})}).then(o=>o.text()).then(o=>{console.log(o),"ok"==o&&(window.location=`${url}/home`)})}function guest(){fetch("/api_loin",{method:"POST",body:JSON.stringify({name:"123",pass:"123"})}).then(o=>o.text()).then(o=>{console.log(o),"ok"==o&&(window.location=`${url}/home`)})}',
    "index_full.html": 
        r'<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <!-- <link rel="stylesheet" href="file/style.css"> --> <style> * { margin: 0; padding: 0; -moz-user-select: none !important; -webkit-touch-callout: none !important; -webkit-user-select: none !important; -khtml-user-select: none !important; -moz-user-select: none !important; -ms-user-select: none !important; user-select: none !important; } body { background-color: rgb(114, 104, 104); height: 100vh; } .main { height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; } .main .camvar { width: 100%; background-color: white; background-repeat: no-repeat; background-size: contain; position: relative; z-index: 1; } .main canvas { position: relative; height: inherit; width: inherit; z-index: 10; position: absolute; left: 0; } .main .chat { margin-top: 10px; /* margin-bottom:; */ } .main #lam_ { position: absolute; height: 100%; width: 100%; left: 0; top: 0; z-index: 10 } .main .button { margin-top: 10px; } </style></head><body> <div class="main"> <div class="camvar"> <img src="/strim" width="100%" height="100%"> <canvas></canvas> <!-- <div id="lam_"></div> --> </div> </div> <script src="file/index.js"></script></body></html>'
}
# đóng toàn bộ file
# index.close()
# index_js.close()
# loin.close()
# loin_js.close()

# cài đặc độ phân giả 
resolution_uses = {'x': 852 , 'y': 480}
resolution = {
    '480' : {'y': 480, 'x': 852 },
    '720' : {'x': 1280,'y': 720},
    'hd': {'x': 1920, 'y': 1080},
}


user = {

}

andim = [
    {'name': "hieu" , 'pass_': "1772005", "role": "andim"},
    {'name': "123" , 'pass_': "123", "role": "guest"},

]

app = Flask(__name__)

def get_random_string(length = 20):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# kiểm tra là đã đăng nhập hay chưa
def chest(request, role =["all"]):
    cookie = request.cookies.get('user')
    try:
        use = user[cookie]
        if use['role'] in role or "all" in role:
            return True
    except KeyError:
        return False
    return False

@app.route('/home')
def home():
    if chest(request, role = ['andim' , 'guest']):
        return files['index.html']

    else:
        return r"""
            <script>
                
                window.location = `${window.location.origin}`
             </script>
        """

@app.route('/home_full')
def home_full():
    if chest(request, role = ['andim' , 'guest']):
        return files['index_full.html']

    else:
        return r"""
            <script>
                
                window.location = `${window.location.origin}`
             </script>
        """

@app.route('/')
def index():
    return files['loin.html']

@app.route('/api_loin' , methods=['POST'])
def loin():
    json_ = json.loads(request.data)
    print(json_)
    name = json_['name']
    pass_ = json_['pass']
    


    # set cookies 
    for i in andim:
        if i['name'] == name and i['pass_'] == pass_:
            re = make_response("ok")
            cookie = get_random_string()
            re.set_cookie("user",cookie )
            user[cookie] = {"name": i['name'] , "role": i['role']}
            return re
    
    return

# return frames

@app.route('/strim', methods=['GET'])
def strim():
    if chest(request):
        return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    else: return ''

def generate_frames():
    while True:
        im1 = PIL.ImageGrab.grab()

        # im1 = pyautogui.screenshot()
        img = numpy.asarray(im1)
        img = img[:, :, ::-1]
        img = cv2.resize(src=img, dsize=(resolution_uses['y'],resolution_uses['x']))

        ret,buffer=cv2.imencode('.jpg',img)
        frame = buffer.tobytes()

        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        # break



# điều kiển chuât 
@app.route('/mou_api' , methods = ['POST'])
def mouse_controller():
    request_ = request
    if chest(request ):
        json_ = json.loads(request_.data)
        print(json_, end='                                                      \r')

        # print(json_["x"] , json_["y"])
        X , Y = json_["x"], json_["y"]
        type_ = json_["type"]
        button = int(json_["button"])


        bu = Button.left if button == 0 else Button.right


        # đổi từ pyauto to pynput

        if type_ == 'move':
            mou_con.position = (X, Y)
        elif type_ == 'dow':
            mou_con.position = (X, Y)
            mou_con.press(bu)
        elif type_ == 'up':
            mou_con.position = (X, Y)
            mou_con.release(bu)
        elif type_ == 'wheel':
            dx = -(int(json_["dX"]) * 1 / 100)
            dy = -(int(json_["dY"])  * 1 / 100)
            mou_con.position = (X, Y)
            mou_con.scroll(dx , dy)

        return 'ok'

    else:
        return ''

# điều khiền bàn phím
@app.route('/key_api', methods = ['POST'])
def key_controller():
    # global key_replace
    request_ = request
    if chest(request , ['andim']):

        json_ = json.loads(request_.data)
        # print(json_, end='                                                      \r')

        key = int(json_['key'])
        type_ = json_['type']
        
        if type_ != 'up':
            # print('nhấn')
            key_con.press(key_pynput[key])
        else:
            # print('thả')
            key_con.release(key_pynput[key])
        
        # print(json_ , end="                        \r" , flush=True)

        return ''

    else:
        return ''

@app.route('/size', methods = ['POST','GET'])
def get_Resolution():

    global resolution_uses

    if request.method == 'GET': # lấy kính thướng màn hình
        im1 = pyautogui.screenshot()
        width, height = im1.size
        #852×480
        return {'x': width , 'y': height}

    elif request.method == 'POST': # thay đổi độ phân giả video
        if chest(request, ['andim']):
            json_ = json.loads(request.data)

            name = json_['resolution']

            # print(resolution[name])

            resolution_uses = resolution[name]


            return 'ok'



@app.route('/file/<name>')# lấy các file cần thiết
def return_files(name):
    if name in files.keys():
        return files[name]
    else:
        return ''

@app.route('/notly', methods = ['POST'])
def notly():
    if chest(request, ['andim']):
        json_ = json.loads(request.data)
        print(json_)

        toa.show_toast( json_['title'],json_['message'] , duration = 10)
        return 'ok'


    else: 
        return ''

@app.route('/all_user')
def all_user():
    if chest(request, ['andim']):
        return user
    else:
        return 'bạn không có thẩm quền'


@app.route('/')
def get_file():
    return ''

if __name__ == '__main__':

    # logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run(host='0.0.0.0' , port=5000)
