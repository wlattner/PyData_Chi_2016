# automatically generated, do not modify

# namespace: fbs

import flatbuffers

class Column(object):
    __slots__ = ['_tab']

    # Column
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Column
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # Column
    def Values(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PrimitiveArray import PrimitiveArray
            obj = PrimitiveArray()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Column
    def MetadataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Column
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

# /// This should (probably) be JSON
    # Column
    def UserMetadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def ColumnStart(builder): builder.StartObject(5)
def ColumnAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def ColumnAddValues(builder, values): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def ColumnAddMetadataType(builder, metadataType): builder.PrependUint8Slot(2, metadataType, 0)
def ColumnAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def ColumnAddUserMetadata(builder, userMetadata): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(userMetadata), 0)
def ColumnEnd(builder): return builder.EndObject()
