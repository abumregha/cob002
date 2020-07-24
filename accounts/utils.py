from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from bidi import algorithm as bidialg


def render_to_pdf(template_src, context_dic={}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    pdf = pisa.CreatePDF(bidialg.get_display(html, base_dir="L"), result)
    result = BytesIO()
    # X = BytesIO(html.encode("ISO-8859-1"))
    # # .decode('unicode-escape')
    # # print(X.getvalue())
    # pdf = pisa.pisaDocument(X, result)
    if not pdf.error:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None