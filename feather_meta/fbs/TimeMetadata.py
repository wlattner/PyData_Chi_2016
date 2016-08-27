# automatically generated, do not modify

# namespace: fbs

import flatbuffers

class TimeMetadata(object):
    __slots__ = ['_tab']

    # TimeMetadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TimeMetadata
    def Unit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def TimeMetadataStart(builder): builder.StartObject(1)
def TimeMetadataAddUnit(builder, unit): builder.PrependInt8Slot(0, unit, 0)
def TimeMetadataEnd(builder): return builder.EndObject()
