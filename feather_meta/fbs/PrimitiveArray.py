# automatically generated, do not modify

# namespace: fbs

import flatbuffers

class PrimitiveArray(object):
    __slots__ = ['_tab']

    # PrimitiveArray
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PrimitiveArray
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # PrimitiveArray
    def Encoding(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

# /// Relative memory offset of the start of the array data excluding the size
# /// of the metadata
    # PrimitiveArray
    def Offset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

# /// The number of logical values in the array
    # PrimitiveArray
    def Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

# /// The number of observed nulls
    # PrimitiveArray
    def NullCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

# /// The total size of the actual data in the file
    # PrimitiveArray
    def TotalBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def PrimitiveArrayStart(builder): builder.StartObject(6)
def PrimitiveArrayAddType(builder, type): builder.PrependInt8Slot(0, type, 0)
def PrimitiveArrayAddEncoding(builder, encoding): builder.PrependInt8Slot(1, encoding, 0)
def PrimitiveArrayAddOffset(builder, offset): builder.PrependInt64Slot(2, offset, 0)
def PrimitiveArrayAddLength(builder, length): builder.PrependInt64Slot(3, length, 0)
def PrimitiveArrayAddNullCount(builder, nullCount): builder.PrependInt64Slot(4, nullCount, 0)
def PrimitiveArrayAddTotalBytes(builder, totalBytes): builder.PrependInt64Slot(5, totalBytes, 0)
def PrimitiveArrayEnd(builder): return builder.EndObject()
