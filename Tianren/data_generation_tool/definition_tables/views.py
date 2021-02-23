from django.http import HttpResponse
from .generate_tables.generate_table import generate_tables, create_table


def index(request):
    table_name: str = request.GET.get('tableName')
    generate_tables()
    return HttpResponse(f"<h1> Generating tables </h1>"
                        f"<h1> Go to Admin to generate table </h1>")
