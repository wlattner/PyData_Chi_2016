# automatically generated, do not modify

# namespace: fbs

import flatbuffers

class TimestampMetadata(object):
    __slots__ = ['_tab']

    # TimestampMetadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TimestampMetadata
    def Unit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

# /// Timestamp data is assumed to be UTC, but the time zone is stored here for
# /// presentation as localized
    # TimestampMetadata
    def Timezone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def TimestampMetadataStart(builder): builder.StartObject(2)
def TimestampMetadataAddUnit(builder, unit): builder.PrependInt8Slot(0, unit, 0)
def TimestampMetadataAddTimezone(builder, timezone): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(timezone), 0)
def TimestampMetadataEnd(builder): return builder.EndObject()
