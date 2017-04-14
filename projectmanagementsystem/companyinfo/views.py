# coding: utf-8

#from django.shortcuts import render
#from companyinfo.forms import *

# Create your views here.




# Create your views here.
#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.utils import timezone
from companyinfo.models import CompanyInfo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from companyinfo.pagingHelper import pagingHelper
from django.http import HttpResponse
#from django.core.urlresolvers import reverse



#===========================================================================================

#import pdb; pdb.set_trace()
rowsPerPage = 10

def home(request):
    boardList = CompanyInfo.objects.order_by('-id')[0:10]
    current_page =1
    totalCnt = CompanyInfo.objects.all().count()

    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
    print 'totalPageList', totalPageList

    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'current_page':current_page ,'totalPageList':totalPageList} )

#===========================================================================================
def show_write_form(request):
    return render_to_response('writeBoard.html')

#===========================================================================================

@csrf_exempt
def DoWriteBoard(request):
	br = CompanyInfo (
		technology_select = request.POST['technology_select'],
		url = request.POST['url'],
		business = request.POST['business'],
		name = request.POST['name'],
		contact = request.POST['contact'],
		phone = request.POST['phone'],
		email = request.POST['email'],
		position = request.POST['position'],
		reference = request.POST['reference'],
		created_date = timezone.now(),
		hits = 0
	)
	br.save()

	# 다시 조회
	url = '/listSpecificPageWork?current_page=1'
	return HttpResponseRedirect(url)

#===========================================================================================
def viewWork(request):
    pk= request.GET['memo_id']
    #print 'pk='+ pk
    boardData = CompanyInfo.objects.get(id=pk)
    #print boardData.memo

    # Update DataBase
    print 'boardData.hits', boardData.hits
    CompanyInfo.objects.filter(id=pk).update(hits = boardData.hits + 1)

    return render_to_response('viewMemo.html', {'memo_id': request.GET['memo_id'],
                                                'current_page':request.GET['current_page'],
                                                'searchStr': request.GET['searchStr'],
                                                'boardData': boardData } )

#===========================================================================================
def listSpecificPageWork(request):
    current_page = request.GET['current_page']
    totalCnt = CompanyInfo.objects.all().count()
    print 'current_page=', current_page

    # 페이지를 가지고 범위 데이터를 조회한다 => raw SQL 사용함
    #boardList = CompanyInfo.objects.raw('SELECT * FROM(SELECT * ceil( rownum / %s ) as page FROM ( SELECT * FROM companyinfo_companyinfo  ORDER BY id DESC )) WHERE page = %s'), [rowsPerPage, current_page]
    #boardList = CompanyInfo.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil( @rownum / %s ) as page FROM ( SELECT id,technology_select,NAME,BUSINESS,REFERENCE,CONTACT,POSITION,PHONE,EMAIL,URL,CREATED_DATE,HITS FROM companyinfo_companyinfo  ORDER BY id DESC ) X ) Z WHERE page = %s', [rowsPerPage, current_page])
    a = int(current_page)-1
    b = int(rowsPerPage)
    c = a*b
    boardList = CompanyInfo.objects.raw('SELECT id,technology_select,NAME,BUSINESS,REFERENCE,CONTACT,POSITION,PHONE,EMAIL,URL,CREATED_DATE,HITS FROM companyinfo_companyinfo LIMIT %s,%s',[int(c),int(b)])

    print  'boardList=',boardList, 'count()=', totalCnt

    # 전체 페이지를 구해서 전달...
    pagingHelperIns = pagingHelper();

    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

    print 'totalPageList', totalPageList
    print 'ddd'
    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'current_page':int(current_page) ,'totalPageList':totalPageList} )

#===========================================================================================

def updatePage(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    searchStr = request.GET['searchStr']

    #totalCnt = CompanyInfo.objects.all().count()
    print 'memo_id', memo_id
    print 'current_page', current_page
    print 'searchStr', searchStr

    boardData = CompanyInfo.objects.get(id=memo_id)

    return render_to_response('viewForUpdate.html', {'memo_id': request.GET['memo_id'],
                                                'current_page':request.GET['current_page'],
                                                'searchStr': request.GET['searchStr'],
                                                'boardData': boardData } )

#===========================================================================================
@csrf_exempt
def updateBoard(request):
    memo_id = request.POST['memo_id']
    current_page = request.POST['current_page']
    searchStr = request.POST['searchStr']

    print '#### updateBoard ######'
    print 'memo_id', memo_id
    print 'current_page', current_page
    print 'searchStr', searchStr

    # Update DataBase
    CompanyInfo.objects.filter(id=memo_id).update(
                                                  technology_select = request.POST['technology_select'],
                                                  url = request.POST['url'],
												  business = request.POST['business'],
												  name = request.POST['name'],
												  contact = request.POST['contact'],
												  email = request.POST['email'],
												  position = request.POST['position'],
                                                  reference = request.POST['reference']
                                                  )

    # Display Page => POST 요청은 redirection!
    url = '/listSpecificPageWork?current_page=' + str(current_page)
    return HttpResponseRedirect(url)


#===========================================================================================
def DeleteSpecificRow(request):
    memo_id = request.GET['memo_id']
    current_page = request.GET['current_page']
    print '#### DeleteSpecificRow ######'
    print 'memo_id', memo_id
    print 'current_page', current_page

    p = CompanyInfo.objects.get(id=memo_id)
    p.delete()

    # Display Page
    # 마지막 메모를 삭제하는 경우, 페이지를 하나 줄임.
    totalCnt = CompanyInfo.objects.all().count()
    pagingHelperIns = pagingHelper();

    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
    print 'totalPages', totalPageList

    if( int(current_page) in totalPageList):
        print 'current_page No Change'
        current_page=current_page
    else:
        current_page= int(current_page)-1
        print 'current_page--'

    url = '/listSpecificPageWork?current_page=' + str(current_page)
    return HttpResponseRedirect(url)

#===========================================================================================
@csrf_exempt
def searchWithSubject(request):
    searchStr = request.POST['searchStr']
    print 'searchStr', searchStr

    url = '/listSearchedSpecificPageWork?searchStr=' + searchStr +'&pageForView=1'
    return HttpResponseRedirect(url)


#===========================================================================================
def listSearchedSpecificPageWork(request):
    searchStr = request.GET['searchStr']
    pageForView = request.GET['pageForView']
    print 'listSearchedSpecificPageWork:searchStr', searchStr, 'pageForView=', pageForView

    #boardList = CompanyInfo.objects.filter(subject__contains=searchStr)
    #print  'boardList=',boardList

    totalCnt = CompanyInfo.objects.filter(name__contains=searchStr).count()
    print  'totalCnt=',totalCnt

    pagingHelperIns = pagingHelper();
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

    # like 구문 적용방법
    boardList = CompanyInfo.objects.raw("""SELECT Z.* FROM ( SELECT X.*, ceil( limit / %s) as page FROM ( SELECT id,technology_select,NAME,BUSINESS,REFERENCE,CONTACT,POSITION,PHONE,EMAIL,URL,CREATED_DATE,HITS FROM companyinfo_companyinfo WHERE NAME LIKE '%%'||%s||'%%' ORDER BY ID DESC) X ) Z WHERE page = %s""", [rowsPerPage, searchStr, pageForView])

    print'boardList=',boardList

    return render_to_response('listSearchedSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
                                                        'pageForView':int(pageForView) ,'searchStr':searchStr, 'totalPageList':totalPageList} )

#===========================================================================================
