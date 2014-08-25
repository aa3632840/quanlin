from django.test import TestCase
from django.nose import FastFixtureTestCase
# from quanlin.models import Danpin,Taocan,TaocanDetail
# # Create your tests here.

class testobjectTest(FastFixtureTestCase):
        
    def test_Invalide(self):
            print 1
            print 1
            print 1
            print 1
            print 1
            print 1
            print 1

    # def testTaocanModel(self):
    #     print '---------testTaocanModel'    
    #     taocan = Taocan(bianhao="123*2")
    #     danpin = Danpin(bianhao="123")
    #     taocan.save()
    #     danpin.save()
    #     tc_detail = TaocanDetail(danpin=danpin,count=6)
    #     tc_detail.save()
    #     print tc_detail
    #     print taocan.taocandetail
    #     taocan.taocandetail.add(tc_detail)
    #     print taocan.taocandetail.count()
    #     print taocan,danpin,taocan.taocandetail

    #     print '---------testTaocanModel'        

# class objectTest2(TestCase):
#     def test_syncTaocanX(self):
#         print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>syncTaocan'
#         taocan = Taocan(bianhao="123*2")
#         taocan.save()
#         for i in range(1,7):
#             danpin = Danpin(bianhao="%s*%s" %(i,i))
#             danpin.save()
#             print 'createDanpin==>', danpin
#             tc_detail = TaocanDetail.objects.get_or_create(danpin=danpin,count=i)[0]
#             print tc_detail.id
#             taocan.taocandetail.add(tc_detail)

#             #taocan.addTaocanDetail(danpin,i)

#         print taocan,taocan.taocandetail.count()
#         # for d in taocan.taocandetail:
#         #     print d

#         print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>syncTaocan'
        