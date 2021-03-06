from flask import Blueprint, request, jsonify
from backend.models.product import Product
from backend.models.type import Type
from backend import db_app

product_bp = Blueprint('product', __name__)


@product_bp.route('/api/product', methods=['GET'])
def get_product_info():
    args_dic = {}
    oid = request.args.get('sellerid')
    pname = request.args.get('productname')
    firsttype = request.args.get('type1')
    secondtype = request.args.get('type2')
    type_ids = None
    if firsttype is not None:
        tp_args_dic = {'type1': firsttype}
        if secondtype is not None:
            tp_args_dic['type2'] = secondtype
        type_ids = [typ['typeid'] for typ in Type.get_type(tp_args_dic)]

    if oid is not None:
        args_dic['oid'] = oid
    if pname is not None:
        args_dic['pname'] = pname
    if type_ids is not None:
        args_dic['types'] = type_ids

    products = Product.get_product(args_dic)

    typeid_list = [product['typeid'] for product in products]
    types = Type.get_type({'typeid_list': typeid_list})
    types_dic = {}
    for typ in types:
        types_dic[typ['typeid']] = typ

    for product in products:
        product['type1'] = types_dic[product['typeid']]['type1']
        product['type2'] = types_dic[product['typeid']]['type2']

    return jsonify({'data': products})


@product_bp.route('/api/product', methods=['PUT'])
def put_product_info():
    prid = request.args.get('uid', type=int)
    product = Product().query.filter_by(pid=prid).first()
    type1 = request.form.get('type1')
    type2 = request.form.get('type2')
    types = [typ['typeid'] for typ in Type.get_type({'type1': type1, 'type2': type2})]
    if len(types) == 0:
        return jsonify({'status': 'fail'})

    type_id = types[0]
    if product == None:
        return jsonify({'status': 'fail'})
    else:
        product.iName = request.form.get('productname')
        product.typeID = type_id
        product.iPrice = request.form.get('price')
        product.remain = request.form.get('remain')
        product.description = request.form.get('description')
        db_app.session.commit()
        return jsonify({'status': 'success'})


@product_bp.route('/api/product', methods=['POST'])
def add_product_info():
    type1 = request.form.get('type1')
    type2 = request.form.get('type2')
    types = [typ['typeid'] for typ in Type.get_type({'type1': type1, 'type2': type2})]
    if len(types) == 0:
        return jsonify({'status': 'fail'})

    type_id = types[0]
    product = Product(
        iName=request.form.get('productname'),
        Type_typeID=type_id,
        iPrice=request.form.get('price'),
        remain=request.form.get('remain'),
        description=request.form.get('description'),
        Official_user_official_userID=request.form.get('sellerid')
    )
    db_app.session.add(product)
    db_app.session.commit()
    return jsonify({'status': 'success'})


@product_bp.route('/api/product', methods=['DELETE'])
def del_product_info():
    prid = request.args.get('uid', type=int)
    product = Product().query.filter_by(itemID=prid).first()
    if product == None:
        return jsonify({'status': 'fail'})
    else:
        db_app.session.delete(product)
        db_app.session.commit()
        return jsonify({'status': 'success'})
