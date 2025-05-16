from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer
from products.models import Product

# Define Arabic analyzer
arabic_analyzer = analyzer(
    'arabic_custom',
    tokenizer='standard',
    filter=['lowercase', 'arabic_normalization', 'arabic_stemmer'],
    char_filter=["html_strip"]
)

# Define index settings
product_index = Index('products')
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
@product_index.doc_type
class ProductDocument(Document):
    name = fields.TextField(analyzer=arabic_analyzer)
    brand = fields.TextField(analyzer=arabic_analyzer)
    category = fields.TextField(analyzer='standard')
    nutrition_facts = fields.TextField(analyzer='standard')
    price = fields.FloatField()

    class Django:
        model = Product
