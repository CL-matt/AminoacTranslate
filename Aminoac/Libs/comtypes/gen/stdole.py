from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    OLE_COLOR, FONTITALIC, IPictureDisp, FontEvents,
    OLE_YPOS_CONTAINER, IDispatch, IFontDisp, OLE_YSIZE_CONTAINER,
    Unchecked, FONTUNDERSCORE, OLE_XPOS_CONTAINER, StdPicture,
    OLE_XSIZE_CONTAINER, Library, OLE_XPOS_PIXELS, Gray,
    _check_version, IFontEventsDisp, OLE_YSIZE_PIXELS, OLE_CANCELBOOL,
    Font, OLE_HANDLE, Default, Checked, COMMETHOD, IPicture,
    Monochrome, FONTSIZE, OLE_XSIZE_PIXELS, FONTBOLD,
    OLE_OPTEXCLUSIVE, Color, DISPPARAMS, IUnknown, DISPMETHOD,
    OLE_YSIZE_HIMETRIC, OLE_ENABLEDEFAULTBOOL, GUID, VARIANT_BOOL,
    FONTSTRIKETHROUGH, typelib_path, dispid, OLE_YPOS_HIMETRIC,
    EXCEPINFO, OLE_XSIZE_HIMETRIC, StdFont, _lcid, HRESULT,
    IEnumVARIANT, Picture, IFont, VgaColor, BSTR, FONTNAME,
    OLE_YPOS_PIXELS, OLE_XPOS_HIMETRIC, DISPPROPERTY, CoClass
)


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


__all__ = [
    'OLE_COLOR', 'OLE_YSIZE_HIMETRIC', 'OLE_ENABLEDEFAULTBOOL',
    'FONTITALIC', 'FONTSTRIKETHROUGH', 'IPictureDisp', 'FontEvents',
    'typelib_path', 'OLE_YPOS_CONTAINER', 'IFontDisp',
    'OLE_YSIZE_CONTAINER', 'OLE_YPOS_HIMETRIC', 'Unchecked',
    'FONTUNDERSCORE', 'OLE_XSIZE_HIMETRIC', 'OLE_XPOS_CONTAINER',
    'StdFont', 'StdPicture', 'OLE_XSIZE_CONTAINER', 'Library',
    'OLE_XPOS_PIXELS', 'Gray', 'Picture', 'IFontEventsDisp',
    'LoadPictureConstants', 'OLE_YSIZE_PIXELS', 'IFont', 'VgaColor',
    'OLE_CANCELBOOL', 'Font', 'OLE_HANDLE', 'Default', 'Checked',
    'IPicture', 'Monochrome', 'FONTSIZE', 'FONTNAME',
    'OLE_YPOS_PIXELS', 'OLE_XSIZE_PIXELS', 'FONTBOLD', 'OLE_TRISTATE',
    'OLE_XPOS_HIMETRIC', 'OLE_OPTEXCLUSIVE', 'Color'
]

