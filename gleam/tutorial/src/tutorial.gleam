import hello_world as t1
import modules as t2
import unqualified_imports as t3
import ints as t4
import floats as t5
import number_formats as t6
import equality as t7
import strings as t8
import bools as t9
import assignments as t10
import type_aliases as t11
import blocks as t12
import list as t13
import higher_order_function as t14
import anonymous_function as t15
import function_captures as t16
import pipeline as t17
import case_expressions as t18
import variable_patterns as t19
import string_patterns as t20
import list_patterns as t21
import recursion as t22
import tail_calls as t23
import list_recursion as t24
import multi_subjects as t25
import alternative_pattern as t26
import pattern_aliases as t27
import guards as t28

pub fn basics(){
  t1.hello_world()
  t2.modules()
  t3.unqualifed_imports()
  t4.ints()
  t5.floats()
  t6.number_formats()
  t7.equality()
  t8.strings()
  t9.bools()
  t10.assignments()
  t11.type_aliases()
  t12.blocks()
  t13.lists()
}

pub fn functions(){
  t14.higher_order_fn()
  t15.anon_fn()
  t16.fn_captures()
  t17.pipeline()
}

pub fn flow_control(){
  t18.case_expression()
  t19.variable_pattern()
  t20.string_pattern()
  t21.list_pattern()
  t22.recursion()
  t23.tail_call()
  t24.list_recursion()
  t25.multiple_subjects()
  t26.alternative_pattern()
  t27.pattern_aliases()
  t28.guards()
}

pub fn main() {
  flow_control()
}
