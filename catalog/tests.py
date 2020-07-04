from django.test import TestCase
from serializers.authorSerializer import BulkCreateListSerializer
from .extractAuthors import getAuthorSet

# Create your tests here.

class AuthorBulkSerializerTestCase(TestCase):

    def testSerializer(self):
        authorSet = getAuthorSet()
        authList = list()

        for authTup in authorSet:
            authDict = dict()
            authDict['first_name'] = authTup[0]
            authDict['last_name'] = authTup[1]
            authList.append(authDict)

        serializer = BulkCreateListSerializer(authList)
        self.assertTrue(serializer.is_valid())



