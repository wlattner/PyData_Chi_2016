# automatically generated, do not modify

# namespace: fbs

import flatbuffers

class CategoryMetadata(object):
    __slots__ = ['_tab']

    # CategoryMetadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// The category codes are presumed to be integers that are valid indexes into
# /// the levels array
    # CategoryMetadata
    def Levels(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PrimitiveArray import PrimitiveArray
            obj = PrimitiveArray()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CategoryMetadata
    def Ordered(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def CategoryMetadataStart(builder): builder.StartObject(2)
def CategoryMetadataAddLevels(builder, levels): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(levels), 0)
def CategoryMetadataAddOrdered(builder, ordered): builder.PrependBoolSlot(1, ordered, 0)
def CategoryMetadataEnd(builder): return builder.EndObject()
