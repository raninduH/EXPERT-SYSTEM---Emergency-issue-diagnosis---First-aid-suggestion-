# bc_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def cut_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.cut_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.cut_diagnosis_heuristic: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cut_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.cut_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.cut_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('questions', 'observed_symptoms', context,
                                  (rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.cut_diagnosis_normal: got unexpected plan from when clause 3"
                    if context.lookup_data('bleedingCode') in context.lookup_data('symptom')  :
                      with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                        (rule.pattern(4),
                                         rule.pattern(5),
                                         rule.pattern(6),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "bc.cut_diagnosis_normal: got unexpected plan from when clause 5"
                          mark6 = context.mark(True)
                          if rule.pattern(7).match_data(context, context,
                                  'Since bleeding is occurring, there is a high probability to be a cut somewhere in the body.'):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cut_treat_aid(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'equipment', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.cut_treat_aid: got unexpected plan from when clause 1"
            with engine.prove('facts', 'equipment', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.cut_treat_aid: got unexpected plan from when clause 2"
                with engine.prove('questions', 'first_aid_equipment', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.cut_treat_aid: got unexpected plan from when clause 3"
                    if context.lookup_data('bandagesCode') in context.lookup_data('equipment') and context.lookup_data('AntisepticCode') in context.lookup_data('equipment'):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def burn_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.burn_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.burn_diagnosis_heuristic: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def burn_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.burn_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.burn_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('questions', 'observed_symptoms', context,
                                  (rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.burn_diagnosis_normal: got unexpected plan from when clause 3"
                    if context.lookup_data('burningSensationCode') in context.lookup_data('symptom')  :
                      mark5 = context.mark(True)
                      if rule.pattern(4).match_data(context, context,
                              'Burn'  ):
                        context.end_save_all_undo()
                        mark6 = context.mark(True)
                        if rule.pattern(5).match_data(context, context,
                                ('Burning Sensation',)  ):
                          context.end_save_all_undo()
                          with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                            (rule.pattern(4),
                                             rule.pattern(5),
                                             rule.pattern(6),)) \
                            as gen_7:
                            for x_7 in gen_7:
                              assert x_7 is None, \
                                "bc.burn_diagnosis_normal: got unexpected plan from when clause 7"
                              mark8 = context.mark(True)
                              if rule.pattern(7).match_data(context, context,
                                      'Because a burning sensation implies that the body was exposed to some unnecessary heat.'  ):
                                context.end_save_all_undo()
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark8)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark6)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def burn_treat_advice(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'equipment', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.burn_treat_advice: got unexpected plan from when clause 1"
            with engine.prove('questions', 'first_aid_equipment', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.burn_treat_advice: got unexpected plan from when clause 2"
                if context.lookup_data('waterCode') in context.lookup_data('equipment'):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def burn_treat_alternative_advice(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'equipment', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.burn_treat_alternative_advice: got unexpected plan from when clause 1"
            with engine.prove('facts', 'equipment', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.burn_treat_alternative_advice: got unexpected plan from when clause 2"
                with engine.prove('questions', 'first_aid_equipment', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.burn_treat_alternative_advice: got unexpected plan from when clause 3"
                    if context.lookup_data('dryClothCode') in context.lookup_data('equipment') or context.lookup_data('nonStickGauzeCode') in context.lookup_data('equipment'):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fracture_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.fracture_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.fracture_diagnosis_heuristic: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fracture_diagnosis_normal_one(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.fracture_diagnosis_normal_one: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.fracture_diagnosis_normal_one: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.fracture_diagnosis_normal_one: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'issue_type_question', context,
                                      (rule.pattern(6),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.fracture_diagnosis_normal_one: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'observed_symptoms', context,
                                          (rule.pattern(7),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.fracture_diagnosis_normal_one: got unexpected plan from when clause 5"
                            if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('deformityCode') in context.lookup_data('symptom')  :
                              mark7 = context.mark(True)
                              if rule.pattern(8).match_data(context, context,
                                      'Fracture'  ):
                                context.end_save_all_undo()
                                mark8 = context.mark(True)
                                if rule.pattern(9).match_data(context, context,
                                        ('Swelling', 'Pain', 'Deformity')  ):
                                  context.end_save_all_undo()
                                  with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                    (rule.pattern(8),
                                                     rule.pattern(9),
                                                     rule.pattern(10),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "bc.fracture_diagnosis_normal_one: got unexpected plan from when clause 9"
                                      mark10 = context.mark(True)
                                      if rule.pattern(11).match_data(context, context,
                                              'This diagnosis was made because the observed symptoms of swelling, pain, and deformity strongly suggest a fracture based on their conditional probabilities.'  ):
                                        context.end_save_all_undo()
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark10)
                                else: context.end_save_all_undo()
                                context.undo_to_mark(mark8)
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark7)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fracture_diagnosis_normal_two(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.fracture_diagnosis_normal_two: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.fracture_diagnosis_normal_two: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.fracture_diagnosis_normal_two: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'issue_type_question', context,
                                      (rule.pattern(6),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.fracture_diagnosis_normal_two: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'observed_symptoms', context,
                                          (rule.pattern(7),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.fracture_diagnosis_normal_two: got unexpected plan from when clause 5"
                            if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('deformityCode') not in context.lookup_data('symptom')  :
                              mark7 = context.mark(True)
                              if rule.pattern(8).match_data(context, context,
                                      'Fracture'  ):
                                context.end_save_all_undo()
                                mark8 = context.mark(True)
                                if rule.pattern(9).match_data(context, context,
                                        ('Swelling', 'Pain')  ):
                                  context.end_save_all_undo()
                                  with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                    (rule.pattern(8),
                                                     rule.pattern(9),
                                                     rule.pattern(10),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "bc.fracture_diagnosis_normal_two: got unexpected plan from when clause 9"
                                      mark10 = context.mark(True)
                                      if rule.pattern(11).match_data(context, context,
                                              'This diagnosis was made because the observed symptoms of swelling and bruising are commonly associated with fractures, as indicated by their conditional probabilities.'  ):
                                        context.end_save_all_undo()
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark10)
                                else: context.end_save_all_undo()
                                context.undo_to_mark(mark8)
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark7)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def shock_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.shock_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.shock_diagnosis_heuristic: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def shock_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.shock_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.shock_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('questions', 'issue_type_question', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.shock_diagnosis_normal: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'observed_symptoms', context,
                                      (rule.pattern(5),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.shock_diagnosis_normal: got unexpected plan from when clause 4"
                        if context.lookup_data('dizzinessCode') in context.lookup_data('symptom') and context.lookup_data('weak_pulseCode') in context.lookup_data('symptom')  :
                          mark6 = context.mark(True)
                          if rule.pattern(6).match_data(context, context,
                                  'Shock'  ):
                            context.end_save_all_undo()
                            mark7 = context.mark(True)
                            if rule.pattern(7).match_data(context, context,
                                    ('Dizziness', 'Weak Pulse')  ):
                              context.end_save_all_undo()
                              with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                (rule.pattern(6),
                                                 rule.pattern(7),
                                                 rule.pattern(8),)) \
                                as gen_8:
                                for x_8 in gen_8:
                                  assert x_8 is None, \
                                    "bc.shock_diagnosis_normal: got unexpected plan from when clause 8"
                                  mark9 = context.mark(True)
                                  if rule.pattern(9).match_data(context, context,
                                          'Due to the patient having Dizziness followed by Weak pulse, it is a high likelihood that the patient is suffering from shock.'  ):
                                    context.end_save_all_undo()
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark9)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark7)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def concussion_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.concussion_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.concussion_diagnosis_heuristic: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def concussion_diagnosis_normal_one(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'activity', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'symptom', context,
                                      (rule.pattern(6),
                                       rule.pattern(7),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'issue_type_question', context,
                                          (rule.pattern(8),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'observed_symptoms', context,
                                              (rule.pattern(9),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 6"
                                if context.lookup_data('confusionCode') in context.lookup_data('symptom') and context.lookup_data('headacheCode') in context.lookup_data('symptom')  :
                                  if context.lookup_data('nauseaCode') in context.lookup_data('symptom')  :
                                    with engine.prove('questions', 'exposed_activity', context,
                                                      (rule.pattern(10),)) \
                                      as gen_9:
                                      for x_9 in gen_9:
                                        assert x_9 is None, \
                                          "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 9"
                                        if context.lookup_data('headInjuryCode') in context.lookup_data('activity')  :
                                          mark11 = context.mark(True)
                                          if rule.pattern(11).match_data(context, context,
                                                  'Concussion'  ):
                                            context.end_save_all_undo()
                                            mark12 = context.mark(True)
                                            if rule.pattern(12).match_data(context, context,
                                                    ('Head injury', 'Confusion', 'Headache', 'Nausea',) ):
                                              context.end_save_all_undo()
                                              with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                                (rule.pattern(11),
                                                                 rule.pattern(12),
                                                                 rule.pattern(13),)) \
                                                as gen_13:
                                                for x_13 in gen_13:
                                                  assert x_13 is None, \
                                                    "bc.concussion_diagnosis_normal_one: got unexpected plan from when clause 13"
                                                  mark14 = context.mark(True)
                                                  if rule.pattern(14).match_data(context, context,
                                                          'Because the patient had a head injury and showcases symptoms like confusion, headache, and nausea.'  ):
                                                    context.end_save_all_undo()
                                                    rule.rule_base.num_bc_rule_successes += 1
                                                    yield
                                                  else: context.end_save_all_undo()
                                                  context.undo_to_mark(mark14)
                                            else: context.end_save_all_undo()
                                            context.undo_to_mark(mark12)
                                          else: context.end_save_all_undo()
                                          context.undo_to_mark(mark11)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def concussion_diagnosis_normal_two(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'activity', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'symptom', context,
                                      (rule.pattern(6),
                                       rule.pattern(7),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'issue_type_question', context,
                                          (rule.pattern(8),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'observed_symptoms', context,
                                              (rule.pattern(9),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 6"
                                if context.lookup_data('confusionCode') in context.lookup_data('symptom') and context.lookup_data('headacheCode') in context.lookup_data('symptom')  :
                                  if context.lookup_data('nauseaCode') in context.lookup_data('symptom')  :
                                    with engine.prove('questions', 'exposed_activity', context,
                                                      (rule.pattern(10),)) \
                                      as gen_9:
                                      for x_9 in gen_9:
                                        assert x_9 is None, \
                                          "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 9"
                                        if context.lookup_data('noIdeaInjuryCode') in context.lookup_data('activity')  :
                                          mark11 = context.mark(True)
                                          if rule.pattern(11).match_data(context, context,
                                                  'Concussion'  ):
                                            context.end_save_all_undo()
                                            mark12 = context.mark(True)
                                            if rule.pattern(12).match_data(context, context,
                                                    ('Confusion', 'Headache', 'Nausea')):
                                              context.end_save_all_undo()
                                              with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                                (rule.pattern(11),
                                                                 rule.pattern(12),
                                                                 rule.pattern(13),)) \
                                                as gen_13:
                                                for x_13 in gen_13:
                                                  assert x_13 is None, \
                                                    "bc.concussion_diagnosis_normal_two: got unexpected plan from when clause 13"
                                                  mark14 = context.mark(True)
                                                  if rule.pattern(14).match_data(context, context,
                                                          'Even though you are not sure about the patient\'s head injury, still due to showcasing symptoms like confusion, headache, and nausea, concussion might be the case.'  ):
                                                    context.end_save_all_undo()
                                                    rule.rule_base.num_bc_rule_successes += 1
                                                    yield
                                                  else: context.end_save_all_undo()
                                                  context.undo_to_mark(mark14)
                                            else: context.end_save_all_undo()
                                            context.undo_to_mark(mark12)
                                          else: context.end_save_all_undo()
                                          context.undo_to_mark(mark11)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def concussion_diagnosis_normal_three(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'activity', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'symptom', context,
                                      (rule.pattern(6),
                                       rule.pattern(7),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'issue_type_question', context,
                                          (rule.pattern(8),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'exposed_activity', context,
                                              (rule.pattern(9),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 6"
                                if context.lookup_data('headInjuryCode') in context.lookup_data('activity')  :
                                  with engine.prove('questions', 'observed_symptoms', context,
                                                    (rule.pattern(10),)) \
                                    as gen_8:
                                    for x_8 in gen_8:
                                      assert x_8 is None, \
                                        "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 8"
                                      if context.lookup_data('confusionCode') in context.lookup_data('symptom') and context.lookup_data('headacheCode') in context.lookup_data('symptom') and context.lookup_data('nauseaCode') not in context.lookup_data('symptom') :
                                        mark10 = context.mark(True)
                                        if rule.pattern(11).match_data(context, context,
                                                'Concussion'  ):
                                          context.end_save_all_undo()
                                          mark11 = context.mark(True)
                                          if rule.pattern(12).match_data(context, context,
                                                  ('Head injury', 'Confusion', 'Headache',) ):
                                            context.end_save_all_undo()
                                            with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                              (rule.pattern(11),
                                                               rule.pattern(12),
                                                               rule.pattern(13),)) \
                                              as gen_12:
                                              for x_12 in gen_12:
                                                assert x_12 is None, \
                                                  "bc.concussion_diagnosis_normal_three: got unexpected plan from when clause 12"
                                                mark13 = context.mark(True)
                                                if rule.pattern(14).match_data(context, context,
                                                        'Because the patient had a head injury and showcases symptoms like confusion and headache.'  ):
                                                  context.end_save_all_undo()
                                                  rule.rule_base.num_bc_rule_successes += 1
                                                  yield
                                                else: context.end_save_all_undo()
                                                context.undo_to_mark(mark13)
                                          else: context.end_save_all_undo()
                                          context.undo_to_mark(mark11)
                                        else: context.end_save_all_undo()
                                        context.undo_to_mark(mark10)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bee_sting_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.bee_sting_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.bee_sting_diagnosis_heuristic: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        " "  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bee_sting_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.bee_sting_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.bee_sting_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('questions', 'issue_type_question', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.bee_sting_diagnosis_normal: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'observed_symptoms', context,
                                      (rule.pattern(5),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.bee_sting_diagnosis_normal: got unexpected plan from when clause 4"
                        if context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('painCode') in context.lookup_data('symptom')  :
                          mark6 = context.mark(True)
                          if rule.pattern(6).match_data(context, context,
                                  'Bee Sting'  ):
                            context.end_save_all_undo()
                            mark7 = context.mark(True)
                            if rule.pattern(7).match_data(context, context,
                                    ('Swelling', 'Pain',)  ):
                              context.end_save_all_undo()
                              with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                (rule.pattern(6),
                                                 rule.pattern(7),
                                                 rule.pattern(8),)) \
                                as gen_8:
                                for x_8 in gen_8:
                                  assert x_8 is None, \
                                    "bc.bee_sting_diagnosis_normal: got unexpected plan from when clause 8"
                                  mark9 = context.mark(True)
                                  if rule.pattern(9).match_data(context, context,
                                          'Because the patient showcases the symptoms of Swelling followed by pain'  ):
                                    context.end_save_all_undo()
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark9)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark7)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def allergic_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.allergic_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.allergic_diagnosis_heuristic: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        " "  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def allergic_diagnosis_normal_one(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.allergic_diagnosis_normal_one: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.allergic_diagnosis_normal_one: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.allergic_diagnosis_normal_one: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'issue_type_question', context,
                                      (rule.pattern(6),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.allergic_diagnosis_normal_one: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'observed_symptoms', context,
                                          (rule.pattern(7),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.allergic_diagnosis_normal_one: got unexpected plan from when clause 5"
                            if context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom') and context.lookup_data('chestPainCode') in context.lookup_data('symptom')  :
                              mark7 = context.mark(True)
                              if rule.pattern(8).match_data(context, context,
                                      'Allergy'  ):
                                context.end_save_all_undo()
                                mark8 = context.mark(True)
                                if rule.pattern(9).match_data(context, context,
                                        ('Swelling', 'Breathing Difficulty', 'Chest Pain',)  ):
                                  context.end_save_all_undo()
                                  with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                    (rule.pattern(8),
                                                     rule.pattern(9),
                                                     rule.pattern(10),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "bc.allergic_diagnosis_normal_one: got unexpected plan from when clause 9"
                                      mark10 = context.mark(True)
                                      if rule.pattern(11).match_data(context, context,
                                              'Because the patient is showcasing Swellings followed by breathing difficulty and chest pain'  ):
                                        context.end_save_all_undo()
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark10)
                                else: context.end_save_all_undo()
                                context.undo_to_mark(mark8)
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark7)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def allergic_diagnosis_normal_two(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.allergic_diagnosis_normal_two: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.allergic_diagnosis_normal_two: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.allergic_diagnosis_normal_two: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'issue_type_question', context,
                                      (rule.pattern(6),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.allergic_diagnosis_normal_two: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'observed_symptoms', context,
                                          (rule.pattern(7),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.allergic_diagnosis_normal_two: got unexpected plan from when clause 5"
                            if context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom') and context.lookup_data('chestPainCode') not in context.lookup_data('symptom')  :
                              mark7 = context.mark(True)
                              if rule.pattern(8).match_data(context, context,
                                      'Allergy'  ):
                                context.end_save_all_undo()
                                mark8 = context.mark(True)
                                if rule.pattern(9).match_data(context, context,
                                        ('Swelling', 'Breathing Difficulty',)  ):
                                  context.end_save_all_undo()
                                  with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                    (rule.pattern(8),
                                                     rule.pattern(9),
                                                     rule.pattern(10),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "bc.allergic_diagnosis_normal_two: got unexpected plan from when clause 9"
                                      mark10 = context.mark(True)
                                      if rule.pattern(11).match_data(context, context,
                                              'Because the patient is showcasing Swellings followed by breathing difficulty'  ):
                                        context.end_save_all_undo()
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark10)
                                else: context.end_save_all_undo()
                                context.undo_to_mark(mark8)
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark7)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def heart_attack_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.heart_attack_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.heart_attack_diagnosis_heuristic: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        " "  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def heart_attack_diagnosis(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.heart_attack_diagnosis: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.heart_attack_diagnosis: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.heart_attack_diagnosis: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'symptom', context,
                                      (rule.pattern(6),
                                       rule.pattern(7),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.heart_attack_diagnosis: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'issue_type_question', context,
                                          (rule.pattern(8),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.heart_attack_diagnosis: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'observed_symptoms', context,
                                              (rule.pattern(9),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc.heart_attack_diagnosis: got unexpected plan from when clause 6"
                                if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom')  :
                                  if context.lookup_data('sweatingCode') in context.lookup_data('symptom') and context.lookup_data('chestPainCode') in context.lookup_data('symptom')  :
                                    total_prob_of_denominator = 1  
                                    conditional_prob_numerator_conditional_prob_val = 1  
                                    mark11 = context.mark(True)
                                    if rule.pattern(10).match_data(context, context,
                                            'Heart Attack'  ):
                                      context.end_save_all_undo()
                                      mark12 = context.mark(True)
                                      if rule.pattern(11).match_data(context, context,
                                              ('Chest Pain', 'Pain', 'Breathing Difficulty', 'Sweating',)   ):
                                        context.end_save_all_undo()
                                        with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                          (rule.pattern(10),
                                                           rule.pattern(11),
                                                           rule.pattern(12),)) \
                                          as gen_13:
                                          for x_13 in gen_13:
                                            assert x_13 is None, \
                                              "bc.heart_attack_diagnosis: got unexpected plan from when clause 13"
                                            mark14 = context.mark(True)
                                            if rule.pattern(13).match_data(context, context,
                                                    'Because chest pain followed by shortness of breath and sweating are major symptoms of a heart attack'  ):
                                              context.end_save_all_undo()
                                              rule.rule_base.num_bc_rule_successes += 1
                                              yield
                                            else: context.end_save_all_undo()
                                            context.undo_to_mark(mark14)
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark12)
                                    else: context.end_save_all_undo()
                                    context.undo_to_mark(mark11)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def hypothermia_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.hypothermia_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.hypothermia_diagnosis_heuristic: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        " "  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def hypothermia_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'activity', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 3"
                    with engine.prove('facts', 'symptom', context,
                                      (rule.pattern(6),
                                       rule.pattern(7),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'issue_type_question', context,
                                          (rule.pattern(8),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'exposed_activity', context,
                                              (rule.pattern(9),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 6"
                                if context.lookup_data('coldExposureCode') in context.lookup_data('activities')  :
                                  with engine.prove('questions', 'observed_symptoms', context,
                                                    (rule.pattern(10),)) \
                                    as gen_8:
                                    for x_8 in gen_8:
                                      assert x_8 is None, \
                                        "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 8"
                                      if context.lookup_data('shiveringCode') in context.lookup_data('symptom') and context.lookup_data('slurredSpeechCode') in context.lookup_data('symptom')  :
                                        if context.lookup_data('confusionCode') in context.lookup_data('symptom')  :
                                          mark11 = context.mark(True)
                                          if rule.pattern(11).match_data(context, context,
                                                  'Hypothermia'  ):
                                            context.end_save_all_undo()
                                            mark12 = context.mark(True)
                                            if rule.pattern(12).match_data(context, context,
                                                    ('Cold exposure', 'Shivering', 'Slurred Speech', 'Confusion',)  ):
                                              context.end_save_all_undo()
                                              with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                                (rule.pattern(11),
                                                                 rule.pattern(12),
                                                                 rule.pattern(13),)) \
                                                as gen_13:
                                                for x_13 in gen_13:
                                                  assert x_13 is None, \
                                                    "bc.hypothermia_diagnosis_normal: got unexpected plan from when clause 13"
                                                  mark14 = context.mark(True)
                                                  if rule.pattern(14).match_data(context, context,
                                                          'Because the patient who experienced some cold exposure is showcasing symptoms like shivering, slurred speech, and confusion.'  ):
                                                    context.end_save_all_undo()
                                                    rule.rule_base.num_bc_rule_successes += 1
                                                    yield
                                                  else: context.end_save_all_undo()
                                                  context.undo_to_mark(mark14)
                                            else: context.end_save_all_undo()
                                            context.undo_to_mark(mark12)
                                          else: context.end_save_all_undo()
                                          context.undo_to_mark(mark11)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def choking_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.choking_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.choking_diagnosis_heuristic: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        " "  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def choking_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.choking_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.choking_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('questions', 'issue_type_question', context,
                                  (rule.pattern(4),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.choking_diagnosis_normal: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'observed_symptoms', context,
                                      (rule.pattern(5),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.choking_diagnosis_normal: got unexpected plan from when clause 4"
                        if context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom') and context.lookup_data('coughingCode') in context.lookup_data('symptom')    :
                          mark6 = context.mark(True)
                          if rule.pattern(6).match_data(context, context,
                                  'Choking'  ):
                            context.end_save_all_undo()
                            mark7 = context.mark(True)
                            if rule.pattern(7).match_data(context, context,
                                    ('Coughing', 'Breathing Difficulty',)  ):
                              context.end_save_all_undo()
                              with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                (rule.pattern(6),
                                                 rule.pattern(7),
                                                 rule.pattern(8),)) \
                                as gen_8:
                                for x_8 in gen_8:
                                  assert x_8 is None, \
                                    "bc.choking_diagnosis_normal: got unexpected plan from when clause 8"
                                  mark9 = context.mark(True)
                                  if rule.pattern(9).match_data(context, context,
                                          'Because the patient is coughing and showing breathing difficulties.'  ):
                                    context.end_save_all_undo()
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark9)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark7)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def choking_treat_advice_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.choking_treat_advice_normal: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def choking_treat_advice_alt(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.choking_treat_advice_alt: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def snake_bite_diagnosis_heuristic(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.snake_bite_diagnosis_heuristic: got unexpected plan from when clause 1"
            with engine.prove('questions', 'issue_type_question', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.snake_bite_diagnosis_heuristic: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(2).match_data(context, context,
                        " "  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def snake_bite_diagnosis_normal(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'symptom', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.snake_bite_diagnosis_normal: got unexpected plan from when clause 1"
            with engine.prove('facts', 'symptom', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.snake_bite_diagnosis_normal: got unexpected plan from when clause 2"
                with engine.prove('facts', 'symptom', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.snake_bite_diagnosis_normal: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'issue_type_question', context,
                                      (rule.pattern(6),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.snake_bite_diagnosis_normal: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'observed_symptoms', context,
                                          (rule.pattern(7),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "bc.snake_bite_diagnosis_normal: got unexpected plan from when clause 5"
                            if context.lookup_data('punctureCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('discolorationCode') in context.lookup_data('symptom')   :
                              mark7 = context.mark(True)
                              if rule.pattern(8).match_data(context, context,
                                      'Snake Bite'  ):
                                context.end_save_all_undo()
                                mark8 = context.mark(True)
                                if rule.pattern(9).match_data(context, context,
                                        ('Puncture Wound', 'Swelling', 'Discoloration',)  ):
                                  context.end_save_all_undo()
                                  with engine.prove(rule.rule_base.root_name, 'bc_cond_prob', context,
                                                    (rule.pattern(8),
                                                     rule.pattern(9),
                                                     rule.pattern(10),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "bc.snake_bite_diagnosis_normal: got unexpected plan from when clause 9"
                                      mark10 = context.mark(True)
                                      if rule.pattern(11).match_data(context, context,
                                              "Because the patient has a puncture wound, swellings, and discoloration."  ):
                                        context.end_save_all_undo()
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark10)
                                else: context.end_save_all_undo()
                                context.undo_to_mark(mark8)
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark7)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def conditional_probability(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        total_prob_of_denominator = 1  
        conditional_prob_numerator_conditional_prob_val = 1 
        with engine.prove('facts', 'probability', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_3:
          for x_3 in gen_3:
            assert x_3 is None, \
              "bc.conditional_probability: got unexpected plan from when clause 3"
            total_prob_of_denominator = context.lookup_data('val')  
            with engine.prove('facts', 'cond_probability', context,
                              (rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_5:
              for x_5 in gen_5:
                assert x_5 is None, \
                  "bc.conditional_probability: got unexpected plan from when clause 5"
                if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list')  :
                  conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2') 
            with engine.prove('facts', 'probability', context,
                              (rule.pattern(3),
                               rule.pattern(5),)) \
              as gen_8:
              for x_8 in gen_8:
                assert x_8 is None, \
                  "bc.conditional_probability: got unexpected plan from when clause 8"
                uncertanity = float(context.lookup_data('issue_prob') * conditional_prob_numerator_conditional_prob_val) / total_prob_of_denominator  
                mark10 = context.mark(True)
                if rule.pattern(6).match_data(context, context,
                        float(uncertanity)  ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark10)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def missing_equipment_check(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'first_aid_equipment', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.missing_equipment_check: got unexpected plan from when clause 1"
            required_equipments_code_list = []
            with engine.prove('facts', 'issue_to_equipment', context,
                              (rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc.missing_equipment_check: got unexpected plan from when clause 3"
                required_equipments_code_list.append(context.lookup_data('required_equipments_code'))
            having_equipments = []
            with engine.prove('facts', 'equipment', context,
                              (rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_6:
              for x_6 in gen_6:
                assert x_6 is None, \
                  "bc.missing_equipment_check: got unexpected plan from when clause 6"
                if context.lookup_data('equipmentCode') in context.lookup_data('having_equipments_code_list'):
                  having_equipments.append(context.lookup_data('equipment'))
            required_equipment_list = []
            with engine.prove('facts', 'equipment', context,
                              (rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_10:
              for x_10 in gen_10:
                assert x_10 is None, \
                  "bc.missing_equipment_check: got unexpected plan from when clause 10"
                if context.lookup_data('equipmentCode') in required_equipments_code_list:
                  required_equipment_list.append(context.lookup_data('equipment'))
            missing_equip_list = [item for item in required_equipment_list if item not in having_equipments]
            mark14 = context.mark(True)
            if rule.pattern(5).match_data(context, context,
                    list(missing_equip_list)):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark14)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def outdoor_cut_advice(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.outdoor_cut_advice: got unexpected plan from when clause 1"
            with engine.prove('facts', 'location_to_code', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.outdoor_cut_advice: got unexpected plan from when clause 2"
                with engine.prove('questions', 'current_location', context,
                                  (rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.outdoor_cut_advice: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(4).match_data(context, context,
                            "In outdoor locations, ensure the area is safe from further injury sources and sanitize hands if possible before administering first aid."):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def workplace_burn_advice(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('facts', 'issue', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc.workplace_burn_advice: got unexpected plan from when clause 1"
            with engine.prove('facts', 'location_to_code', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc.workplace_burn_advice: got unexpected plan from when clause 2"
                with engine.prove('questions', 'current_location', context,
                                  (rule.pattern(3),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "bc.workplace_burn_advice: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'issue_type_question', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "bc.workplace_burn_advice: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc')
  
  bc_rule.bc_rule('cut_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  cut_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Cut'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(" "),),
                  (),
                  (pattern.pattern_literal('Cut'),
                   contexts.variable('cutCode'),))
  
  bc_rule.bc_rule('cut_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  cut_diagnosis_normal, None,
                  (pattern.pattern_literal('Cut'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Bleeding'),
                   contexts.variable('bleedingCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   pattern.pattern_literal('Cut'),
                   pattern.pattern_literal(('Bleeding',)),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('cut_treat_aid', This_rule_base, 'first_aid',
                  cut_treat_aid, None,
                  (pattern.pattern_literal('Cut'),
                   pattern.pattern_literal("Clean the wound, apply antiseptic, and bandage it to stop bleeding."),),
                  (),
                  (pattern.pattern_literal('Bandages'),
                   contexts.variable('bandagesCode'),
                   pattern.pattern_literal('Antiseptic'),
                   contexts.variable('AntisepticCode'),
                   contexts.variable('equipment'),))
  
  bc_rule.bc_rule('burn_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  burn_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Burn'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(" "),),
                  (),
                  (pattern.pattern_literal('Burn'),
                   contexts.variable('burnCode'),))
  
  bc_rule.bc_rule('burn_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  burn_diagnosis_normal, None,
                  (pattern.pattern_literal('Burn'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Burning Sensation'),
                   contexts.variable('burningSensationCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('burn_treat_advice', This_rule_base, 'first_aid',
                  burn_treat_advice, None,
                  (pattern.pattern_literal('Burn'),
                   pattern.pattern_literal("Cool the burn under running water for 10 minutes and cover with a sterile dressing."),),
                  (),
                  (pattern.pattern_literal('Water'),
                   contexts.variable('waterCode'),
                   contexts.variable('equipment'),))
  
  bc_rule.bc_rule('burn_treat_alternative_advice', This_rule_base, 'first_aid',
                  burn_treat_alternative_advice, None,
                  (pattern.pattern_literal('Burn'),
                   pattern.pattern_literal("Cover the burn with a clean, dry cloth (or a non-stick gauze pad). Avoid using ointments on severe burns to prevent shock. Keep the person warm and calm while waiting for emergency services."),),
                  (),
                  (pattern.pattern_literal('Dry Cloth'),
                   contexts.variable('dryClothCode'),
                   pattern.pattern_literal('Non-stick gauze pad'),
                   contexts.variable('nonStickGauzeCode'),
                   contexts.variable('equipment'),))
  
  bc_rule.bc_rule('fracture_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  fracture_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Fracture'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(" "),),
                  (),
                  (pattern.pattern_literal('Fracture'),
                   contexts.variable('fractureCode'),))
  
  bc_rule.bc_rule('fracture_diagnosis_normal_one', This_rule_base, 'diagnosed_decease',
                  fracture_diagnosis_normal_one, None,
                  (pattern.pattern_literal('Fracture'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Swelling'),
                   contexts.variable('swellingCode'),
                   pattern.pattern_literal('Pain'),
                   contexts.variable('painCode'),
                   pattern.pattern_literal('Deformity'),
                   contexts.variable('deformityCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('fracture_diagnosis_normal_two', This_rule_base, 'diagnosed_decease',
                  fracture_diagnosis_normal_two, None,
                  (pattern.pattern_literal('Fracture'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Swelling'),
                   contexts.variable('swellingCode'),
                   pattern.pattern_literal('Pain'),
                   contexts.variable('painCode'),
                   pattern.pattern_literal('Deformity'),
                   contexts.variable('deformityCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('shock_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  shock_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Shock'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(" "),),
                  (),
                  (pattern.pattern_literal('Shock'),
                   contexts.variable('shockCode'),))
  
  bc_rule.bc_rule('shock_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  shock_diagnosis_normal, None,
                  (pattern.pattern_literal('Shock'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Dizziness'),
                   contexts.variable('dizzinessCode'),
                   pattern.pattern_literal('Weak Pulse'),
                   contexts.variable('weak_pulseCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('concussion_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  concussion_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Concussion'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal(" "),),
                  (),
                  (pattern.pattern_literal('Concussion'),
                   contexts.variable('concussionCode'),))
  
  bc_rule.bc_rule('concussion_diagnosis_normal_one', This_rule_base, 'diagnosed_decease',
                  concussion_diagnosis_normal_one, None,
                  (pattern.pattern_literal('Concussion'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Head injury'),
                   contexts.variable('headInjuryCode'),
                   pattern.pattern_literal('Confusion'),
                   contexts.variable('confusionCode'),
                   pattern.pattern_literal('Headache'),
                   contexts.variable('headacheCode'),
                   pattern.pattern_literal('Nausea'),
                   contexts.variable('nauseaCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('activity'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('concussion_diagnosis_normal_two', This_rule_base, 'diagnosed_decease',
                  concussion_diagnosis_normal_two, None,
                  (pattern.pattern_literal('Concussion'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('No idea'),
                   contexts.variable('noIdeaInjuryCode'),
                   pattern.pattern_literal('Confusion'),
                   contexts.variable('confusionCode'),
                   pattern.pattern_literal('Headache'),
                   contexts.variable('headacheCode'),
                   pattern.pattern_literal('Nausea'),
                   contexts.variable('nauseaCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('activity'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('concussion_diagnosis_normal_three', This_rule_base, 'diagnosed_decease',
                  concussion_diagnosis_normal_three, None,
                  (pattern.pattern_literal('Concussion'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Head injury'),
                   contexts.variable('headInjuryCode'),
                   pattern.pattern_literal('Confusion'),
                   contexts.variable('confusionCode'),
                   pattern.pattern_literal('Headache'),
                   contexts.variable('headacheCode'),
                   pattern.pattern_literal('Nausea'),
                   contexts.variable('nauseaCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('activity'),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('bee_sting_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  bee_sting_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Bee Sting'),
                   pattern.pattern_literal(1),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Bee Sting'),
                   contexts.variable('beeStingCode'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('bee_sting_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  bee_sting_diagnosis_normal, None,
                  (pattern.pattern_literal('Bee Sting'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Swelling'),
                   contexts.variable('swellingCode'),
                   pattern.pattern_literal('Pain'),
                   contexts.variable('painCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('allergic_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  allergic_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Allergy'),
                   pattern.pattern_literal(1),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Allergy'),
                   contexts.variable('allergyCode'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('allergic_diagnosis_normal_one', This_rule_base, 'diagnosed_decease',
                  allergic_diagnosis_normal_one, None,
                  (pattern.pattern_literal('Allergy'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Swelling'),
                   contexts.variable('swellingCode'),
                   pattern.pattern_literal('Breathing Difficulty'),
                   contexts.variable('breathingDifficultyCode'),
                   pattern.pattern_literal('Chest Pain'),
                   contexts.variable('chestPainCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('allergic_diagnosis_normal_two', This_rule_base, 'diagnosed_decease',
                  allergic_diagnosis_normal_two, None,
                  (pattern.pattern_literal('Allergy'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Swelling'),
                   contexts.variable('swellingCode'),
                   pattern.pattern_literal('Breathing Difficulty'),
                   contexts.variable('breathingDifficultyCode'),
                   pattern.pattern_literal('Chest Pain'),
                   contexts.variable('chestPainCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('heart_attack_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  heart_attack_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Heart Attack'),
                   pattern.pattern_literal(1),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Heart Attack'),
                   contexts.variable('heartAttackCode'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('heart_attack_diagnosis', This_rule_base, 'diagnosed_decease',
                  heart_attack_diagnosis, None,
                  (pattern.pattern_literal('Heart Attack'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Chest Pain'),
                   contexts.variable('chestPainCode'),
                   pattern.pattern_literal('Pain'),
                   contexts.variable('painCode'),
                   pattern.pattern_literal('Breathing Difficulty'),
                   contexts.variable('breathingDifficultyCode'),
                   pattern.pattern_literal('Sweating'),
                   contexts.variable('sweatingCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('hypothermia_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  hypothermia_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Hypothermia'),
                   pattern.pattern_literal(1),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Hypothermia'),
                   contexts.variable('hypothermiaCode'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('hypothermia_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  hypothermia_diagnosis_normal, None,
                  (pattern.pattern_literal('Hypothermia'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Cold exposure'),
                   contexts.variable('coldExposureCode'),
                   pattern.pattern_literal('Shivering'),
                   contexts.variable('shiveringCode'),
                   pattern.pattern_literal('Slurred Speech'),
                   contexts.variable('slurredSpeechCode'),
                   pattern.pattern_literal('Confusion'),
                   contexts.variable('confusionCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('activities'),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('choking_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  choking_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Choking'),
                   pattern.pattern_literal(1),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Choking'),
                   contexts.variable('chokingCode'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('choking_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  choking_diagnosis_normal, None,
                  (pattern.pattern_literal('Choking'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Breathing Difficulty'),
                   contexts.variable('breathingDifficultyCode'),
                   pattern.pattern_literal('Coughing'),
                   contexts.variable('coughingCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('choking_treat_advice_normal', This_rule_base, 'first_aid',
                  choking_treat_advice_normal, None,
                  (pattern.pattern_literal('Choking'),
                   pattern.pattern_literal("Perform the Heimlich maneuver and seek emergency medical help if the obstruction is not cleared."),),
                  (),
                  (pattern.pattern_literal('Choking'),
                   contexts.variable('chokingCode'),))
  
  bc_rule.bc_rule('choking_treat_advice_alt', This_rule_base, 'first_aid',
                  choking_treat_advice_alt, None,
                  (pattern.pattern_literal('Choking'),
                   pattern.pattern_literal("Lean the person forward and firmly strike their back between the shoulder blades with the palm of your hand. Repeat up to five times or until the object is expelled."),),
                  (),
                  (pattern.pattern_literal('Choking'),
                   contexts.variable('chokingCode'),))
  
  bc_rule.bc_rule('snake_bite_diagnosis_heuristic', This_rule_base, 'diagnosed_decease',
                  snake_bite_diagnosis_heuristic, None,
                  (pattern.pattern_literal('Snake Bite'),
                   pattern.pattern_literal(1),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Snake Bite'),
                   contexts.variable('snakeBiteCode'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('snake_bite_diagnosis_normal', This_rule_base, 'diagnosed_decease',
                  snake_bite_diagnosis_normal, None,
                  (pattern.pattern_literal('Snake Bite'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),),
                  (),
                  (pattern.pattern_literal('Puncture Wound'),
                   contexts.variable('punctureCode'),
                   pattern.pattern_literal('Swelling'),
                   contexts.variable('swellingCode'),
                   pattern.pattern_literal('Discoloration'),
                   contexts.variable('discolorationCode'),
                   pattern.pattern_literal(1),
                   contexts.variable('symptom'),
                   contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),
                   contexts.variable('reason'),))
  
  bc_rule.bc_rule('conditional_probability', This_rule_base, 'bc_cond_prob',
                  conditional_probability, None,
                  (contexts.variable('issue'),
                   contexts.variable('given_symptoms_list'),
                   contexts.variable('uncertanity'),),
                  (),
                  (contexts.variable('given_symptoms_list'),
                   contexts.variable('val'),
                   contexts.variable('given_symptom_name'),
                   contexts.variable('issue'),
                   contexts.variable('val2'),
                   contexts.variable('issue_prob'),
                   contexts.variable('uncertanity'),))
  
  bc_rule.bc_rule('missing_equipment_check', This_rule_base, 'missing_equipment',
                  missing_equipment_check, None,
                  (contexts.variable('issue'),
                   contexts.variable('missing_equip_list'),),
                  (),
                  (contexts.variable('having_equipments_code_list'),
                   contexts.variable('issue'),
                   contexts.variable('required_equipments_code'),
                   contexts.variable('equipment'),
                   contexts.variable('equipmentCode'),
                   contexts.variable('missing_equip_list'),))
  
  bc_rule.bc_rule('outdoor_cut_advice', This_rule_base, 'location_advice',
                  outdoor_cut_advice, None,
                  (pattern.pattern_literal('Cut'),
                   contexts.variable('advice'),),
                  (),
                  (pattern.pattern_literal('Cut'),
                   contexts.variable('cutCode'),
                   pattern.pattern_literal('Outdoor'),
                   contexts.variable('outdoorCode'),
                   contexts.variable('advice'),))
  
  bc_rule.bc_rule('workplace_burn_advice', This_rule_base, 'location_advice',
                  workplace_burn_advice, None,
                  (pattern.pattern_literal('Burn'),
                   pattern.pattern_literal("In the workplace, assess any surrounding hazards, and contact the onsite medical team if available."),),
                  (),
                  (pattern.pattern_literal('Burn'),
                   contexts.variable('burnCode'),
                   pattern.pattern_literal('Workplace'),
                   contexts.variable('workplaceCode'),))


Krb_filename = '..\\bc.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 26), (7, 7)),
    ((27, 32), (8, 8)),
    ((45, 49), (12, 12)),
    ((51, 57), (15, 15)),
    ((58, 63), (17, 17)),
    ((64, 69), (18, 18)),
    ((70, 70), (19, 19)),
    ((71, 78), (21, 21)),
    ((81, 81), (23, 23)),
    ((97, 101), (26, 26)),
    ((103, 109), (28, 28)),
    ((110, 116), (29, 29)),
    ((117, 122), (30, 30)),
    ((123, 123), (31, 31)),
    ((136, 140), (38, 38)),
    ((142, 148), (40, 40)),
    ((149, 154), (41, 41)),
    ((167, 171), (45, 45)),
    ((173, 179), (48, 48)),
    ((180, 185), (50, 50)),
    ((186, 191), (51, 51)),
    ((192, 192), (52, 52)),
    ((195, 195), (55, 55)),
    ((199, 199), (56, 56)),
    ((201, 208), (58, 58)),
    ((211, 211), (60, 60)),
    ((231, 235), (64, 64)),
    ((237, 243), (66, 66)),
    ((244, 249), (67, 67)),
    ((250, 250), (68, 68)),
    ((263, 267), (71, 71)),
    ((269, 275), (73, 73)),
    ((276, 282), (74, 74)),
    ((283, 288), (75, 75)),
    ((289, 289), (76, 76)),
    ((302, 306), (83, 83)),
    ((308, 314), (85, 85)),
    ((315, 320), (86, 86)),
    ((333, 337), (90, 90)),
    ((339, 345), (93, 93)),
    ((346, 352), (94, 94)),
    ((353, 359), (95, 95)),
    ((360, 365), (97, 97)),
    ((366, 371), (98, 98)),
    ((372, 372), (99, 99)),
    ((375, 375), (101, 101)),
    ((379, 379), (102, 102)),
    ((381, 388), (104, 104)),
    ((391, 391), (106, 106)),
    ((411, 415), (110, 110)),
    ((417, 423), (113, 113)),
    ((424, 430), (114, 114)),
    ((431, 437), (115, 115)),
    ((438, 443), (117, 117)),
    ((444, 449), (118, 118)),
    ((450, 450), (119, 119)),
    ((453, 453), (121, 121)),
    ((457, 457), (122, 122)),
    ((459, 466), (124, 124)),
    ((469, 469), (126, 126)),
    ((489, 493), (132, 132)),
    ((495, 501), (134, 134)),
    ((502, 507), (135, 135)),
    ((520, 524), (138, 138)),
    ((526, 532), (141, 141)),
    ((533, 539), (142, 142)),
    ((540, 545), (144, 144)),
    ((546, 551), (145, 145)),
    ((552, 552), (146, 146)),
    ((555, 555), (148, 148)),
    ((559, 559), (149, 149)),
    ((561, 568), (151, 151)),
    ((571, 571), (153, 153)),
    ((591, 595), (159, 159)),
    ((597, 603), (161, 161)),
    ((604, 609), (162, 162)),
    ((622, 626), (166, 166)),
    ((628, 634), (168, 168)),
    ((635, 641), (169, 169)),
    ((642, 648), (170, 170)),
    ((649, 655), (171, 171)),
    ((656, 661), (173, 173)),
    ((662, 667), (175, 175)),
    ((668, 668), (176, 176)),
    ((669, 669), (177, 177)),
    ((670, 675), (179, 179)),
    ((676, 676), (180, 180)),
    ((679, 679), (182, 182)),
    ((683, 683), (183, 183)),
    ((685, 692), (185, 185)),
    ((695, 695), (187, 187)),
    ((715, 719), (191, 191)),
    ((721, 727), (193, 193)),
    ((728, 734), (194, 194)),
    ((735, 741), (195, 195)),
    ((742, 748), (196, 196)),
    ((749, 754), (198, 198)),
    ((755, 760), (200, 200)),
    ((761, 761), (201, 201)),
    ((762, 762), (202, 202)),
    ((763, 768), (204, 204)),
    ((769, 769), (205, 205)),
    ((772, 772), (207, 207)),
    ((776, 776), (208, 208)),
    ((778, 785), (210, 210)),
    ((788, 788), (212, 212)),
    ((808, 812), (217, 217)),
    ((814, 820), (219, 219)),
    ((821, 827), (220, 220)),
    ((828, 834), (221, 221)),
    ((835, 841), (222, 222)),
    ((842, 847), (224, 224)),
    ((848, 853), (226, 226)),
    ((854, 854), (227, 227)),
    ((855, 860), (229, 229)),
    ((861, 861), (230, 230)),
    ((864, 864), (232, 232)),
    ((868, 868), (233, 233)),
    ((870, 877), (235, 235)),
    ((880, 880), (237, 237)),
    ((900, 904), (243, 243)),
    ((906, 912), (245, 245)),
    ((913, 918), (246, 246)),
    ((921, 921), (247, 247)),
    ((937, 941), (250, 250)),
    ((943, 949), (252, 252)),
    ((950, 956), (253, 253)),
    ((957, 962), (255, 255)),
    ((963, 968), (256, 256)),
    ((969, 969), (257, 257)),
    ((972, 972), (259, 259)),
    ((976, 976), (260, 260)),
    ((978, 985), (262, 262)),
    ((988, 988), (264, 264)),
    ((1008, 1012), (271, 271)),
    ((1014, 1020), (273, 273)),
    ((1021, 1026), (274, 274)),
    ((1029, 1029), (275, 275)),
    ((1045, 1049), (278, 278)),
    ((1051, 1057), (280, 280)),
    ((1058, 1064), (281, 281)),
    ((1065, 1071), (282, 282)),
    ((1072, 1077), (284, 284)),
    ((1078, 1083), (285, 285)),
    ((1084, 1084), (286, 286)),
    ((1087, 1087), (289, 289)),
    ((1091, 1091), (290, 290)),
    ((1093, 1100), (292, 292)),
    ((1103, 1103), (294, 294)),
    ((1123, 1127), (298, 298)),
    ((1129, 1135), (300, 300)),
    ((1136, 1142), (301, 301)),
    ((1143, 1149), (302, 302)),
    ((1150, 1155), (304, 304)),
    ((1156, 1161), (305, 305)),
    ((1162, 1162), (306, 306)),
    ((1165, 1165), (309, 309)),
    ((1169, 1169), (310, 310)),
    ((1171, 1178), (312, 312)),
    ((1181, 1181), (314, 314)),
    ((1201, 1205), (320, 320)),
    ((1207, 1213), (322, 322)),
    ((1214, 1219), (323, 323)),
    ((1222, 1222), (324, 324)),
    ((1238, 1242), (327, 327)),
    ((1244, 1250), (329, 329)),
    ((1251, 1257), (330, 330)),
    ((1258, 1264), (331, 331)),
    ((1265, 1271), (332, 332)),
    ((1272, 1277), (334, 334)),
    ((1278, 1283), (336, 336)),
    ((1284, 1284), (337, 337)),
    ((1285, 1285), (338, 338)),
    ((1286, 1286), (340, 340)),
    ((1287, 1287), (341, 341)),
    ((1290, 1290), (343, 343)),
    ((1294, 1294), (344, 344)),
    ((1296, 1303), (346, 346)),
    ((1306, 1306), (348, 348)),
    ((1326, 1330), (354, 354)),
    ((1332, 1338), (356, 356)),
    ((1339, 1344), (357, 357)),
    ((1347, 1347), (358, 358)),
    ((1363, 1367), (361, 361)),
    ((1369, 1375), (363, 363)),
    ((1376, 1382), (364, 364)),
    ((1383, 1389), (365, 365)),
    ((1390, 1396), (366, 366)),
    ((1397, 1402), (368, 368)),
    ((1403, 1408), (370, 370)),
    ((1409, 1409), (371, 371)),
    ((1410, 1415), (373, 373)),
    ((1416, 1416), (374, 374)),
    ((1417, 1417), (375, 375)),
    ((1420, 1420), (377, 377)),
    ((1424, 1424), (378, 378)),
    ((1426, 1433), (380, 380)),
    ((1436, 1436), (382, 382)),
    ((1456, 1460), (389, 389)),
    ((1462, 1468), (391, 391)),
    ((1469, 1474), (392, 392)),
    ((1477, 1477), (393, 393)),
    ((1493, 1497), (397, 397)),
    ((1499, 1505), (399, 399)),
    ((1506, 1512), (400, 400)),
    ((1513, 1518), (402, 402)),
    ((1519, 1524), (404, 404)),
    ((1525, 1525), (405, 405)),
    ((1528, 1528), (407, 407)),
    ((1532, 1532), (408, 408)),
    ((1534, 1541), (410, 410)),
    ((1544, 1544), (412, 412)),
    ((1564, 1568), (415, 415)),
    ((1570, 1576), (417, 417)),
    ((1589, 1593), (421, 421)),
    ((1595, 1601), (423, 423)),
    ((1614, 1618), (427, 427)),
    ((1620, 1626), (429, 429)),
    ((1627, 1632), (430, 430)),
    ((1635, 1635), (431, 431)),
    ((1651, 1655), (433, 433)),
    ((1657, 1663), (435, 435)),
    ((1664, 1670), (436, 436)),
    ((1671, 1677), (437, 437)),
    ((1678, 1683), (439, 439)),
    ((1684, 1689), (441, 441)),
    ((1690, 1690), (442, 442)),
    ((1693, 1693), (444, 444)),
    ((1697, 1697), (445, 445)),
    ((1699, 1706), (447, 447)),
    ((1709, 1709), (449, 449)),
    ((1729, 1733), (462, 462)),
    ((1735, 1735), (464, 464)),
    ((1736, 1736), (465, 465)),
    ((1737, 1743), (467, 467)),
    ((1744, 1744), (468, 468)),
    ((1745, 1752), (471, 471)),
    ((1753, 1753), (472, 472)),
    ((1754, 1754), (473, 473)),
    ((1755, 1761), (475, 475)),
    ((1762, 1762), (477, 477)),
    ((1765, 1765), (478, 478)),
    ((1781, 1785), (482, 482)),
    ((1787, 1792), (484, 484)),
    ((1793, 1793), (486, 486)),
    ((1794, 1800), (488, 488)),
    ((1801, 1801), (489, 489)),
    ((1802, 1802), (491, 491)),
    ((1803, 1809), (493, 493)),
    ((1810, 1810), (494, 494)),
    ((1811, 1811), (495, 495)),
    ((1812, 1812), (497, 497)),
    ((1813, 1819), (499, 499)),
    ((1820, 1820), (500, 500)),
    ((1821, 1821), (501, 501)),
    ((1822, 1822), (503, 503)),
    ((1825, 1825), (504, 504)),
    ((1841, 1845), (508, 508)),
    ((1847, 1853), (510, 510)),
    ((1854, 1860), (511, 511)),
    ((1861, 1866), (514, 514)),
    ((1869, 1869), (517, 517)),
    ((1885, 1889), (520, 520)),
    ((1891, 1897), (522, 522)),
    ((1898, 1904), (523, 523)),
    ((1905, 1910), (525, 525)),
    ((1911, 1916), (526, 526)),
)
