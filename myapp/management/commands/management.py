from django.core.management.base import BaseCommand, CommandError
from myapp.models import Product
import os
from pathlib import Path
import re


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent
        file_path = os.path.join(base_dir, 'Files\\foods.txt')
        data_file = open(file_path, 'r')
        lines = data_file.readlines()
        product_list = {'productId': None, "userId": None, 'helpfulness': None, 'profileName': None, 'score': None,
                        'time': None, 'summary': None, 'text': None}

        for line in lines:
            if line != "\n" and line != "" and line is not None:
                res = re.split(':', line)
                index = re.split('/', res[0])
                product_list[index[1].strip()] = res[1].strip()
            elif product_list['productId'] is not None:
                product = Product(productid=product_list['productId'], userid=product_list['userId'],
                                  helpfulness=product_list['helpfulness'], profilename=product_list['profileName'],
                                  score=product_list['score'], time=product_list['time'],
                                  summary=product_list['summary'], text=product_list['text'])
                product.save()
                print(product_list['productId'] + " has been loaded successfully")
                product_list['productId'] = None
        if product_list['productId'] is not None:
            product = Product(productid=product_list['productId'], userid=product_list['userId'],
                              helpfulness=product_list['helpfulness'], profilename=product_list['profileName'],
                              score=product_list['score'], time=product_list['time'],
                              summary=product_list['summary'], text=product_list['text'])
            product.save()
            print(product_list['productId'] + " has been loaded successfully")
            product_list['productId'] = None
        print("All Model has been Loaded Successfully")
