import os
import sys 
from flask import (
     Flask, 
     request, 
     redirect, 
     url_for, 
     make_response, 
     jsonify, 
     render_template, 
     send_from_directory)

UPLOAD_FOLDER_EGG = './i/image_egg' #ナスの写真用

app = Flask(__name__, static_folder='./i')

@app.route('/')
def index():
    return render_template(
        'top.html',
         enter_images=os.listdir(UPLOAD_FOLDER_EGG)[::-1],
         )

@app.route('/uploadpage')
def changepage():
    return render_template('up.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploads_file():
    # リクエストがポストかどうかの判別
    if request.method == 'POST':
        # ファイルがなかった場合の処理
        if 'upload_files' not in request.files:
            print("ファイルなし")
            return redirect(request.url)

        if request.files.getlist('upload_files')[0].filename:
            #画像オブジェクトを受け取る。
            uploads_files = request.files.getlist('upload_files')
            for uploads_file in uploads_files:
                #それぞれの画像に対してimage_enterまでのパスを定義作成してsaveメソッドを用いて保存する。
                img_path = os.path.join(UPLOAD_FOLDER_EGG, uploads_file.filename)
                uploads_file.save(img_path)
        return redirect('/result')

@app.route('/result')
def result():
    return render_template('result_good.html')

#スクリプトからAPIを叩けるようにします。
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)