import graphene
from graphene import relay
from models import Pagination, Hits, Aggregations, BucketCounter, Bucket, get_buckets

x = get_buckets()

class Query(graphene.ObjectType):

    pagination = graphene.Field(Pagination)
    hits = graphene.Field(Hits)
    aggregations = graphene.Field(Aggregations)

    def resolve_pagination(self, args, context, info):
        return Pagination(count=0, sort="case_id.raw:asc", fromNum=1, page=1, total=9999, pages=8, size=0)

    def resolve_hits(self, args, context, info):
        el = []
        return el

    def resolve_aggregations(self, args, context, info):
        return Aggregations(subjectProjectName=[get_buckets("project.name")])
        
ac_schema = graphene.Schema(query=Query)