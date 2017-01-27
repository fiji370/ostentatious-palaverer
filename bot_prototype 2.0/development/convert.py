__all__ = ['convert']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'a', u'feach', u'g', u'checnum', u'n', u'Magnitude', u'text2num', u'Small'])
@Js
def PyJsHoisted_feach_(w, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'w':w}, var)
    var.registers([u'x', u'w'])
    var.put(u'x', var.get(u'Small').get(var.get(u'w')))
    if (var.get(u'x')!=var.get(u"null")):
        var.put(u'g', (var.get(u'g')+var.get(u'x')))
    else:
        if (var.get(u'w')==Js(u'hundred')):
            var.put(u'g', (var.get(u'g')*Js(100.0)))
        else:
            var.put(u'x', var.get(u'Magnitude').get(var.get(u'w')))
            if (var.get(u'x')!=var.get(u"null")):
                var.put(u'n', (var.get(u'n')+(var.get(u'g')*var.get(u'x'))))
                var.put(u'g', Js(0.0))
            else:
                pass
PyJsHoisted_feach_.func_name = u'feach'
var.put(u'feach', PyJsHoisted_feach_)
@Js
def PyJsHoisted_checnum_(PyJsArg_6173_, this, arguments, var=var):
    var = Scope({u'this':this, u'as':PyJsArg_6173_, u'arguments':arguments}, var)
    var.registers([u'a', u'as'])
    var.put(u'a', var.get(u'as').get(u'value'))
    var.get(u'as').put(u'value', var.get(u'a').callprop(u'replace', JsRegExp(u'/[^\\d.]/g'), Js(u'')))
PyJsHoisted_checnum_.func_name = u'checnum'
var.put(u'checnum', PyJsHoisted_checnum_)
@Js
def PyJsHoisted_text2num_(s, this, arguments, var=var):
    var = Scope({u'this':this, u's':s, u'arguments':arguments}, var)
    var.registers([u's'])
    var.put(u'a', var.get(u's').callprop(u'toString').callprop(u'split', JsRegExp(u'/[\\s-]+/')))
    var.put(u'n', Js(0.0))
    var.put(u'g', Js(0.0))
    var.get(u'a').callprop(u'forEach', var.get(u'feach'))
    return (var.get(u'n')+var.get(u'g'))
PyJsHoisted_text2num_.func_name = u'text2num'
var.put(u'text2num', PyJsHoisted_text2num_)
PyJs_Object_0_ = Js({u'zero':Js(0.0),u'one':Js(1.0),u'two':Js(2.0),u'three':Js(3.0),u'four':Js(4.0),u'five':Js(5.0),u'six':Js(6.0),u'seven':Js(7.0),u'eight':Js(8.0),u'nine':Js(9.0),u'ten':Js(10.0),u'eleven':Js(11.0),u'twelve':Js(12.0),u'thirteen':Js(13.0),u'fourteen':Js(14.0),u'fifteen':Js(15.0),u'sixteen':Js(16.0),u'seventeen':Js(17.0),u'eighteen':Js(18.0),u'nineteen':Js(19.0),u'twenty':Js(20.0),u'thirty':Js(30.0),u'forty':Js(40.0),u'fifty':Js(50.0),u'sixty':Js(60.0),u'seventy':Js(70.0),u'eighty':Js(80.0),u'ninety':Js(90.0)})
var.put(u'Small', PyJs_Object_0_)
PyJs_Object_1_ = Js({u'thousand':Js(1000.0),u'million':Js(1000000.0),u'billion':Js(1000000000.0),u'trillion':Js(1000000000000.0),u'quadrillion':Js(1000000000000000.0),u'quintillion':Js(1e+18),u'sexillion':Js(1e+21),u'septillion':Js(1e+24),u'octillion':Js(1e+27),u'nonillion':Js(1e+30),u'decillion':Js(1e+33)})
var.put(u'Magnitude', PyJs_Object_1_)
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
convert = var.to_python()