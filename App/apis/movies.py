from flask_restful import Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import BaseQuery

from App import dao
from App.models import Movies


class MovieApi(Resource):
    # 定制输入参数
    parser = reqparse.RequestParser()
    parser.add_argument('flag', type=int, required=True, help='必须指定影片类型')
    parser.add_argument('city', default='')
    parser.add_argument('region', default='')
    parser.add_argument('orderby', default='openday')
    parser.add_argument('sort', type=int, default=1)  # 1 降序 ，0 升序
    parser.add_argument('page', type=int, default=1, help='页码必须是数值')
    parser.add_argument('limit', type=int, default=10, help='每页显示的大小必须是数值')

    # 定制输出字段
    out_fields = {
        'returnCode': fields.String(default='0'),
        'returnValue': fields.Nested({
            'backgroundPicture': fields.String(attribute='backgroundpicture'),
            'country': fields.String,
            'director': fields.String,
            'showName': fields.String(attribute='showname'),
            'showNameEn': fields.String(attribute='shownameen'),
            'openTime': fields.DateTime(attribute='openday')
        })
    }

    @marshal_with(out_fields)
    def get(self):
        # 验证请求参数
        args = self.parser.parse_args()
        qs: BaseQuery = dao.query(Movies).filter(Movies.flag == args.get('flag'))
        # qs.order_by(args.get('orderby'))
        # if args.get('orderby') == 1:
        #     qs = qs.order_by('-openday')
        #
        # print('获取总影片数:', len(qs.all()))
        # return {'returnValue': qs.all()}

        sort = args.get('sort')
        qs: BaseQuery = qs.order_by(('-' if sort == 1 else '') + args.get('orderby'))

        # 分页
        pager = qs.paginate(args.get('page'), args.get('limit'))

        print('获取的总影片数：', len(qs.all()))
        return {"returnValue": pager.items}
