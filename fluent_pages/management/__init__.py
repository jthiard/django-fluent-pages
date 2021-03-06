from django.contrib.contenttypes.models import ContentType
from django.db import DEFAULT_DB_ALIAS
from django.db.models import signals, get_models
from django.dispatch import receiver
from fluent_pages.models import UrlNode


@receiver(signals.post_syncdb)
def _on_post_syncdb(app, verbosity=2, db=DEFAULT_DB_ALIAS, **kwargs):
    """
    Prefix the ContentType objects of pagetypes, to make them recognizable.
    Runs automatically at syncdb, and initial south model creation.
    """
    app_models = [m for m in get_models(app) if issubclass(m, UrlNode)]
    for model in app_models:
        update_model_prefix(model, verbosity=verbosity, db=db)


def update_model_prefix(model, db=DEFAULT_DB_ALIAS, verbosity=2):
    """
    Internal function to update all model prefixes.
    """
    prefix = "pagetype:"

    ct = ContentType.objects.get_for_model(model)
    new_name = u"{0} {1}".format(prefix, model._meta.verbose_name_raw).strip()

    if ct.name != new_name:
        # Django 1.4/1.5 compatible .save(update_fields=('name',)) look-a-like
        ContentType.objects.using(db).filter(pk=ct.id).update(name=new_name)

        if verbosity >= 1:
            print(" - Updated ContentType title for {0}.{1}".format(model._meta.app_label, model._meta.object_name))
        return True
    return False
