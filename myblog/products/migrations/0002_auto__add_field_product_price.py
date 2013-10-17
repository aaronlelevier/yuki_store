# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.price'
        db.add_column(u'products_product', 'price',
                      self.gf('django.db.models.fields.FloatField')(default=4.99, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.price'
        db.delete_column(u'products_product', 'price')


    models = {
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'products.color': {
            'Meta': {'ordering': "['name']", 'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'products.emailsignup': {
            'Meta': {'ordering': "['email']", 'object_name': 'EmailSignup'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'products.product': {
            'Meta': {'ordering': "['category', 'name']", 'object_name': 'Product'},
            'best_seller': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'color': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Color']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_picture': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'picture2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '4.99', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'style': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Style']", 'symmetrical': 'False'})
        },
        u'products.style': {
            'Meta': {'ordering': "['name']", 'object_name': 'Style'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['products']