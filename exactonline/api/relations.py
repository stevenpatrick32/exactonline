# vim: set ts=8 sw=4 sts=4 et ai tw=79:
from .manager import Manager


class Relations(Manager):
    resource = 'crm/Accounts'

    def filter(self, relation_code=None, **kwargs):
        # $select=ID,Code,Name
        if 'select' not in kwargs:
            kwargs['select'] = 'ID,Code,Name'

        if relation_code is not None:
            remote_id = self._remote_relation_code(relation_code)
            self._filter_append(kwargs, u'Code eq %s' % (remote_id,))
        return super(Relations, self).filter(**kwargs)

    def _remote_relation_code(self, code):
        return u"'%18s'" % (code.replace("'", "''"),)
