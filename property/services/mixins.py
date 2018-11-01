"""
A module for customized mixins
"""


class FlattenMixin:
    """
    Flattens the specified related objects in this representation while ignoring the keys in
    flatten_ignore. Excepts required flatten attribute and optional flatten_ignore attribute in
    Meta class.
    """
    def to_representation(self, obj):
        """
        A serializer method for changing the output data
        :param obj:
        :return:
        """
        assert hasattr(self.Meta, 'flatten'), (
            'Class {serializer_class} missing "Meta.flatten" attribute'.format(
                serializer_class=self.__class__.__name__
            )
        )
        ignore = getattr(self.Meta, 'flatten_ignore', [])

        data = super(FlattenMixin, self).to_representation(obj)

        for field, serializer_class in self.Meta.flatten:
            serializer = serializer_class(context=self.context)
            obj_data = serializer.to_representation(getattr(obj, field))

            for key in obj_data:
                if key not in ignore:
                    data[key] = obj_data[key]

        return data
