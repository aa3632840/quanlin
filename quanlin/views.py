# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from models import Shipping
from django.template import Context
from django.template import loader
from operator import contains


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


def get_avalide_shipping_line_data(ship_line):
    shipping_values = ship_line.strip().split('\t')

    if len(shipping_values) == 3:
        try:
            out_sid, weight, post_fee = shipping_values
            weight = float(weight)
            post_fee = float(post_fee)
            return out_sid, weight, post_fee
        except Exception, e:
            print e
            return None

    return None


def get_avalide_inavalide_shipping_values_from_lines(shipping_lines):
    """"将输入的数据 进行检查，并返回有效和无效的数据"""
    inavalide_shipping_lines = []
    avalide_shipping_lines = []
    avalide_shipping_out_sid = []

    for ship_line in shipping_lines.split('\n'):
        shipping_values = get_avalide_shipping_line_data(ship_line)
        if shipping_values:
            #去除重复项,并将其放到错误数据中
            if contains(avalide_shipping_out_sid, shipping_values[0]):
                avalide_shipping_out_sid.remove(shipping_values[0])

                for sp_value in avalide_shipping_lines:
                    if sp_value[0] == shipping_values[0]:
                        avalide_shipping_lines.remove(sp_value)
                        inavalide_shipping_lines.append(
                            u'重复项 %s' % str(sp_value))
                        inavalide_shipping_lines.append(
                            u'重复项 %s' % str(shipping_values))
            #如果没有重复项，则添加out_sid到avalide_shipping_out_sid中
            else:
                avalide_shipping_out_sid.append(shipping_values[0])

            avalide_shipping_lines.append(shipping_values)
        else:
            inavalide_shipping_lines.append(ship_line)

    return avalide_shipping_lines, inavalide_shipping_lines


def contact(request):
    shipping_lines = request.REQUEST.get('shipping_lines', '').strip()
    avalide_shipping_lines, inavalide_shipping_lines = \
        get_avalide_inavalide_shipping_values_from_lines(shipping_lines)
    if avalide_shipping_lines:
        exist_shipping_list = []
        unbound_tid_shippings = []
        shipping_list = []
        for shipping_values in avalide_shipping_lines:
            out_sid, weight, post_fee = shipping_values
            #如果已经有此数据
            if Shipping.objects.filter(
                    out_sid=out_sid,
                    weight=weight,
                    post_fee=post_fee).count() > 0:
                    # print u'已有此数据'
                sp = Shipping.objects.get(out_sid=out_sid)
                exist_shipping_list.append(sp)
                #未绑定，但需绑定tid的快递
            elif Shipping.objects.filter(out_sid=out_sid).count() > 0:
                sp = Shipping.objects.get(out_sid=out_sid)
                sp.out_sid, sp.weight, sp.post_fee = shipping_values
                sp.save()
                unbound_tid_shippings.append(sp)
            else:
                #数据库内没有此数据的
                sp = Shipping()
                sp.out_sid, sp.weight, sp.post_fee = shipping_values
                sp.save()
                shipping_list.append(sp)

        template = loader.get_template('quanlin/add_shipping.html')
        context = Context({
            'shipping_list': shipping_list,
            'exist_shipping_list': exist_shipping_list,
            'unbound_tid_shippings': unbound_tid_shippings,
            'inavalide_shipping_lines': inavalide_shipping_lines,
        })
        return HttpResponse(template.render(context))
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm()

    return render(request, 'quanlin/contact.html', {
        'form': form,
    })
