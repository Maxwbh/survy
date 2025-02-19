# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify


def create_slug(sender, instance, signal, *args, **kwargs):
    # check for id and attributes
    if instance.id:
        # get slug information
        slug_name = 'slug'
        slug_from = 'title'
        # save slug if empty
        if not getattr(instance, slug_name, None):
            # create slug
            slug = u'{0:s}'.format(slugify(getattr(instance, slug_from)))
            # set slug
            setattr(instance, slug_name, slug)
            # save instance
            instance.save()
