# automatically generated, do not modify

# namespace: fbs

import flatbuffers

class CTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CTable()
        x.Init(buf, n + offset)
        return x


    # CTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// Some text (or a name) metadata about what the file is, optional
    # CTable
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # CTable
    def NumRows(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CTable
    def Columns(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Column import Column
            obj = Column()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CTable
    def ColumnsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Version number of the Feather format
    # CTable
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

# /// Table metadata (likely JSON), not yet used
    # CTable
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def CTableStart(builder): builder.StartObject(5)
def CTableAddDescription(builder, description): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)
def CTableAddNumRows(builder, numRows): builder.PrependInt64Slot(1, numRows, 0)
def CTableAddColumns(builder, columns): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(columns), 0)
def CTableStartColumnsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CTableAddVersion(builder, version): builder.PrependInt32Slot(3, version, 0)
def CTableAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def CTableEnd(builder): return builder.EndObject()
