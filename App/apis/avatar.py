import os

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage

from App import settings
from App.dao import *
from App.models import User


class UploadApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('picture', type=FileStorage, location='files', required=True, help='提供一个File表单参数')
    parser.add_argument('username', type=str, required=True, help='必须指定用户')

    # 保存上传的文件
    def post(self):
        args = self.parser.parse_args()

        uFile: FileStorage = args.get('img')
        print('上传文件名：', uFile.filename)
        name = args.get('username')
        user = query(User).filter(User.name.__eq__(name)).first()
        session['token'] = user.id
        id = query_id_from_session(user.id)
        print('查找id')
        if id:
            newFileName1 = name + 'big'
            newFileName1 += '.jpg'

            newFileName2 = name + 's' + '.jpg'
            p1 = os.path.join(settings.MEDIA_DIR, newFileName1)
            p2 = os.path.join(settings.MEDIA_DIR, newFileName2)

            print('开始保存', p1)

            uFile.save(p1, 4096)
            uFile.close()

            user.photo_1 = '/static/user_avatar/' + newFileName1
            print('保存完成')

            result = ResizeImage(p1, p2, 80, 80, 'jpg')

            if result:
                user.photo_2 = '/static/user_avatar/' + newFileName2
                save(user)

            return {'msg': '图片上传成功!'}
        return {'msg': '请先登录'}
