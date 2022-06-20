from django.test import TestCase
import uuid
import shortuuid

def TestUuid():
    print(uuid.uuid4())


TestUuid()


def TestShortUuid():
    print(shortuuid.uuid())

TestShortUuid()