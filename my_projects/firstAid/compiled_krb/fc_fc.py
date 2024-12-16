# fc_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def cut_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def cut_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'observed_symptoms', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('bleedingCode') in context.lookup_data('symptom')   :
                  total_prob_of_denominator = 1
                  conditional_prob_numerator_conditional_prob_val = 1
                  mark6 = context.mark(True)
                  if rule.pattern(0).match_data(context, context,
                          'Cut'):
                    context.end_save_all_undo()
                    mark7 = context.mark(True)
                    if rule.pattern(1).match_data(context, context,
                            ('Bleeding',)):
                      context.end_save_all_undo()
                      with knowledge_base.Gen_once if index == 3 \
                               else engine.lookup('facts', 'probability', context,
                                                  rule.foreach_patterns(3)) \
                        as gen_3:
                        for dummy in gen_3:
                          total_prob_of_denominator =  context.lookup_data('val')
                          with engine.lookup('facts', 'cond_probability', context, \
                                             rule.foreach_patterns(4)) \
                            as gen_4:
                            for dummy in gen_4:
                              if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                          with knowledge_base.Gen_once if index == 5 \
                                   else engine.lookup('facts', 'probability', context,
                                                      rule.foreach_patterns(5)) \
                            as gen_5:
                            for dummy in gen_5:
                              uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                              mark15 = context.mark(True)
                              if rule.pattern(2).match_data(context, context,
                                      float(uncertanity)):
                                context.end_save_all_undo()
                                engine.assert_('facts', 'diagnosed_decease',
                                               (rule.pattern(3).as_data(context),
                                                rule.pattern(2).as_data(context),
                                                rule.pattern(4).as_data(context),)),
                                rule.rule_base.num_fc_rules_triggered += 1
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark15)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark7)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark6)
  finally:
    context.done()

def cut_treat(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'first_aid_equipment', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('bandagesCode') in context.lookup_data('equipment') and context.lookup_data('AntisepticCode') in context.lookup_data('equipment'):
                      engine.assert_('facts', 'first_aid',
                                     (rule.pattern(0).as_data(context),
                                      rule.pattern(1).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def burn_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def burn_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'observed_symptoms', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('burningSensationCode') in context.lookup_data('symptom'):
                  total_prob_of_denominator = 1
                  conditional_prob_numerator_conditional_prob_val = 1
                  mark6 = context.mark(True)
                  if rule.pattern(0).match_data(context, context,
                          'Burn'):
                    context.end_save_all_undo()
                    mark7 = context.mark(True)
                    if rule.pattern(1).match_data(context, context,
                            ('Burning Sensation',)):
                      context.end_save_all_undo()
                      with knowledge_base.Gen_once if index == 3 \
                               else engine.lookup('facts', 'probability', context,
                                                  rule.foreach_patterns(3)) \
                        as gen_3:
                        for dummy in gen_3:
                          total_prob_of_denominator =  context.lookup_data('val')
                          with engine.lookup('facts', 'cond_probability', context, \
                                             rule.foreach_patterns(4)) \
                            as gen_4:
                            for dummy in gen_4:
                              if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                          with knowledge_base.Gen_once if index == 5 \
                                   else engine.lookup('facts', 'probability', context,
                                                      rule.foreach_patterns(5)) \
                            as gen_5:
                            for dummy in gen_5:
                              uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                              mark15 = context.mark(True)
                              if rule.pattern(2).match_data(context, context,
                                      float(uncertanity)):
                                context.end_save_all_undo()
                                engine.assert_('facts', 'diagnosed_decease',
                                               (rule.pattern(3).as_data(context),
                                                rule.pattern(2).as_data(context),
                                                rule.pattern(4).as_data(context),)),
                                rule.rule_base.num_fc_rules_triggered += 1
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark15)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark7)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark6)
  finally:
    context.done()

def burn_treat(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'diagnosed_decease', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('waterCode') in context.lookup_data('equipment'):
                  engine.assert_('facts', 'first_aid',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def burn_treat_alternative(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'diagnosed_decease', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'first_aid_equipment', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('dryClothCode') in context.lookup_data('equipment') or context.lookup_data('nonStickGauzeCode') in context.lookup_data('equipment'):
                      engine.assert_('facts', 'first_aid',
                                     (rule.pattern(0).as_data(context),
                                      rule.pattern(1).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fracture_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fracture_diagnosis_normal_one(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'issue_type_question', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'observed_symptoms', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('deformityCode') in context.lookup_data('symptom'):
                          total_prob_of_denominator = 1
                          conditional_prob_numerator_conditional_prob_val = 1
                          mark8 = context.mark(True)
                          if rule.pattern(0).match_data(context, context,
                                  'Fracture'):
                            context.end_save_all_undo()
                            mark9 = context.mark(True)
                            if rule.pattern(1).match_data(context, context,
                                    ('Swelling','Pain','Deformity',)):
                              context.end_save_all_undo()
                              with knowledge_base.Gen_once if index == 5 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  total_prob_of_denominator =  context.lookup_data('val')
                                  with engine.lookup('facts', 'cond_probability', context, \
                                                     rule.foreach_patterns(6)) \
                                    as gen_6:
                                    for dummy in gen_6:
                                      if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                        conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                                  with knowledge_base.Gen_once if index == 7 \
                                           else engine.lookup('facts', 'probability', context,
                                                              rule.foreach_patterns(7)) \
                                    as gen_7:
                                    for dummy in gen_7:
                                      uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                      mark17 = context.mark(True)
                                      if rule.pattern(2).match_data(context, context,
                                              float(uncertanity)):
                                        context.end_save_all_undo()
                                        engine.assert_('facts', 'diagnosed_decease',
                                                       (rule.pattern(3).as_data(context),
                                                        rule.pattern(2).as_data(context),
                                                        rule.pattern(4).as_data(context),)),
                                        rule.rule_base.num_fc_rules_triggered += 1
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark17)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark9)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark8)
  finally:
    context.done()

def fracture_diagnosis_normal_two(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'issue_type_question', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'observed_symptoms', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('deformityCode') not in context.lookup_data('symptom'):
                          total_prob_of_denominator = 1
                          conditional_prob_numerator_conditional_prob_val = 1
                          mark8 = context.mark(True)
                          if rule.pattern(0).match_data(context, context,
                                  'Fracture'):
                            context.end_save_all_undo()
                            mark9 = context.mark(True)
                            if rule.pattern(1).match_data(context, context,
                                    ('Swelling','Pain',)):
                              context.end_save_all_undo()
                              with knowledge_base.Gen_once if index == 5 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  total_prob_of_denominator =  context.lookup_data('val')
                                  with engine.lookup('facts', 'cond_probability', context, \
                                                     rule.foreach_patterns(6)) \
                                    as gen_6:
                                    for dummy in gen_6:
                                      if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                        conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                                  with knowledge_base.Gen_once if index == 7 \
                                           else engine.lookup('facts', 'probability', context,
                                                              rule.foreach_patterns(7)) \
                                    as gen_7:
                                    for dummy in gen_7:
                                      uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                      mark17 = context.mark(True)
                                      if rule.pattern(2).match_data(context, context,
                                              float(uncertanity) ):
                                        context.end_save_all_undo()
                                        engine.assert_('facts', 'diagnosed_decease',
                                                       (rule.pattern(3).as_data(context),
                                                        rule.pattern(2).as_data(context),
                                                        rule.pattern(4).as_data(context),)),
                                        rule.rule_base.num_fc_rules_triggered += 1
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark17)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark9)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark8)
  finally:
    context.done()

def fracture_treat_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'diagnosed_decease', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'first_aid_equipment', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('splintCode') in context.lookup_data('equipment') and context.lookup_data('icePackCode') not in context.lookup_data('equipment'):
                      engine.assert_('facts', 'first_aid',
                                     (rule.pattern(0).as_data(context),
                                      rule.pattern(1).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fracture_treat_two(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'diagnosed_decease', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'first_aid_equipment', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('splintCode') in context.lookup_data('equipment'):
                      if context.lookup_data('icePackCode') in context.lookup_data('equipment'):
                        engine.assert_('facts', 'first_aid',
                                       (rule.pattern(0).as_data(context),
                                        rule.pattern(1).as_data(context),)),
                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def shock_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def shock_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'issue_type_question', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'observed_symptoms', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('dizzinessCode') in context.lookup_data('symptom') and context.lookup_data('weak_pulseCode') in context.lookup_data('symptom'):
                      total_prob_of_denominator = 1
                      conditional_prob_numerator_conditional_prob_val = 1
                      mark7 = context.mark(True)
                      if rule.pattern(0).match_data(context, context,
                              'Shock'):
                        context.end_save_all_undo()
                        mark8 = context.mark(True)
                        if rule.pattern(1).match_data(context, context,
                                ('Dizziness','Weak Pulse',)):
                          context.end_save_all_undo()
                          with knowledge_base.Gen_once if index == 4 \
                                   else engine.lookup('facts', 'probability', context,
                                                      rule.foreach_patterns(4)) \
                            as gen_4:
                            for dummy in gen_4:
                              total_prob_of_denominator =  context.lookup_data('val')
                              with engine.lookup('facts', 'cond_probability', context, \
                                                 rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                    conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                              with knowledge_base.Gen_once if index == 6 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(6)) \
                                as gen_6:
                                for dummy in gen_6:
                                  uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                  mark16 = context.mark(True)
                                  if rule.pattern(2).match_data(context, context,
                                          float(uncertanity) ):
                                    context.end_save_all_undo()
                                    engine.assert_('facts', 'diagnosed_decease',
                                                   (rule.pattern(3).as_data(context),
                                                    rule.pattern(2).as_data(context),
                                                    rule.pattern(4).as_data(context),)),
                                    rule.rule_base.num_fc_rules_triggered += 1
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark16)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark8)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark7)
  finally:
    context.done()

def shock_treat(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def concussion_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def concussion_diagnosis_normal_one(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'activity', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'symptom', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'issue_type_question', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'observed_symptoms', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            if context.lookup_data('confusionCode') in context.lookup_data('symptom') and context.lookup_data('headacheCode') in context.lookup_data('symptom'):
                              if context.lookup_data('nauseaCode') in context.lookup_data('symptom'):
                                with knowledge_base.Gen_once if index == 6 \
                                         else engine.lookup('questions', 'exposed_activity', context,
                                                            rule.foreach_patterns(6)) \
                                  as gen_6:
                                  for dummy in gen_6:
                                    if context.lookup_data('headInjuryCode') in context.lookup_data('activity'):
                                      with knowledge_base.Gen_once if index == 7 \
                                               else engine.lookup('facts', 'cond_probability', context,
                                                                  rule.foreach_patterns(7)) \
                                        as gen_7:
                                        for dummy in gen_7:
                                          engine.assert_('facts', 'diagnosed_decease',
                                                         (rule.pattern(0).as_data(context),
                                                          rule.pattern(1).as_data(context),
                                                          rule.pattern(2).as_data(context),)),
                                          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def concussion_diagnosis_normal_two(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'activity', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'symptom', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'issue_type_question', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'observed_symptoms', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            if context.lookup_data('confusionCode') in context.lookup_data('symptom') and context.lookup_data('headacheCode') in context.lookup_data('symptom'):
                              if context.lookup_data('nauseaCode') in context.lookup_data('symptom'):
                                with knowledge_base.Gen_once if index == 6 \
                                         else engine.lookup('questions', 'exposed_activity', context,
                                                            rule.foreach_patterns(6)) \
                                  as gen_6:
                                  for dummy in gen_6:
                                    if context.lookup_data('noIdeaInjuryCode') in context.lookup_data('activity'):
                                      with knowledge_base.Gen_once if index == 7 \
                                               else engine.lookup('facts', 'cond_probability', context,
                                                                  rule.foreach_patterns(7)) \
                                        as gen_7:
                                        for dummy in gen_7:
                                          engine.assert_('facts', 'diagnosed_decease',
                                                         (rule.pattern(0).as_data(context),
                                                          rule.pattern(1).as_data(context),
                                                          rule.pattern(2).as_data(context),)),
                                          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def concussion_diagnosis_normal_three(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'activity', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'symptom', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'issue_type_question', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'exposed_activity', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            if context.lookup_data('headInjuryCode') in context.lookup_data('activity'):
                              with knowledge_base.Gen_once if index == 6 \
                                       else engine.lookup('questions', 'observed_symptoms', context,
                                                          rule.foreach_patterns(6)) \
                                as gen_6:
                                for dummy in gen_6:
                                  if context.lookup_data('confusionCode') in context.lookup_data('symptom') and context.lookup_data('headacheCode') in context.lookup_data('symptom') and context.lookup_data('nauseaCode') not in context.lookup_data('symptom'):
                                    with knowledge_base.Gen_once if index == 7 \
                                             else engine.lookup('facts', 'cond_probability', context,
                                                                rule.foreach_patterns(7)) \
                                      as gen_7:
                                      for dummy in gen_7:
                                        engine.assert_('facts', 'diagnosed_decease',
                                                       (rule.pattern(0).as_data(context),
                                                        rule.pattern(1).as_data(context),
                                                        rule.pattern(2).as_data(context),)),
                                        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def concussion_treat_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def bee_sting_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def bee_sting_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'issue_type_question', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'observed_symptoms', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') :
                      total_prob_of_denominator = 1
                      conditional_prob_numerator_conditional_prob_val = 1
                      mark7 = context.mark(True)
                      if rule.pattern(0).match_data(context, context,
                              'Bee Sting'):
                        context.end_save_all_undo()
                        mark8 = context.mark(True)
                        if rule.pattern(1).match_data(context, context,
                                ('Swelling','Pain',)):
                          context.end_save_all_undo()
                          with knowledge_base.Gen_once if index == 4 \
                                   else engine.lookup('facts', 'probability', context,
                                                      rule.foreach_patterns(4)) \
                            as gen_4:
                            for dummy in gen_4:
                              total_prob_of_denominator =  context.lookup_data('val')
                              with engine.lookup('facts', 'cond_probability', context, \
                                                 rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                    conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                              with knowledge_base.Gen_once if index == 6 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(6)) \
                                as gen_6:
                                for dummy in gen_6:
                                  uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                  mark16 = context.mark(True)
                                  if rule.pattern(2).match_data(context, context,
                                          float(uncertanity) ):
                                    context.end_save_all_undo()
                                    engine.assert_('facts', 'diagnosed_decease',
                                                   (rule.pattern(3).as_data(context),
                                                    rule.pattern(2).as_data(context),
                                                    rule.pattern(4).as_data(context),)),
                                    rule.rule_base.num_fc_rules_triggered += 1
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark16)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark8)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark7)
  finally:
    context.done()

def bee_sting_treat(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('icePackCode') in context.lookup_data('equipment') and context.lookup_data('antihistamineCode') in context.lookup_data('equipment'):
                  with knowledge_base.Gen_once if index == 3 \
                           else engine.lookup('facts', 'diagnosed_decease', context,
                                              rule.foreach_patterns(3)) \
                    as gen_3:
                    for dummy in gen_3:
                      engine.assert_('facts', 'first_aid',
                                     (rule.pattern(0).as_data(context),
                                      rule.pattern(1).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def allergic_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def allergic_diagnosis_normal_one(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'issue_type_question', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'observed_symptoms', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        if context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom') and context.lookup_data('chestPainCode') in context.lookup_data('symptom'):
                          total_prob_of_denominator = 1
                          conditional_prob_numerator_conditional_prob_val = 1
                          mark8 = context.mark(True)
                          if rule.pattern(0).match_data(context, context,
                                  'Allergy'):
                            context.end_save_all_undo()
                            mark9 = context.mark(True)
                            if rule.pattern(1).match_data(context, context,
                                    ('Swelling','Breathing Difficulty','Chest Pain',)):
                              context.end_save_all_undo()
                              with knowledge_base.Gen_once if index == 5 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  total_prob_of_denominator =  context.lookup_data('val')
                                  with engine.lookup('facts', 'cond_probability', context, \
                                                     rule.foreach_patterns(6)) \
                                    as gen_6:
                                    for dummy in gen_6:
                                      if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                        conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                                  with knowledge_base.Gen_once if index == 7 \
                                           else engine.lookup('facts', 'probability', context,
                                                              rule.foreach_patterns(7)) \
                                    as gen_7:
                                    for dummy in gen_7:
                                      uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                      mark17 = context.mark(True)
                                      if rule.pattern(2).match_data(context, context,
                                              float(uncertanity) ):
                                        context.end_save_all_undo()
                                        engine.assert_('facts', 'diagnosed_decease',
                                                       (rule.pattern(3).as_data(context),
                                                        rule.pattern(2).as_data(context),
                                                        rule.pattern(4).as_data(context),)),
                                        rule.rule_base.num_fc_rules_triggered += 1
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark17)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark9)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark8)
  finally:
    context.done()

def allergic_diagnosis_normal_two(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'issue_type_question', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'observed_symptoms', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        if context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom') and context.lookup_data('chestPainCode') not in context.lookup_data('symptom'):
                          total_prob_of_denominator = 1
                          conditional_prob_numerator_conditional_prob_val = 1
                          mark8 = context.mark(True)
                          if rule.pattern(0).match_data(context, context,
                                  'Allergy'):
                            context.end_save_all_undo()
                            mark9 = context.mark(True)
                            if rule.pattern(1).match_data(context, context,
                                    ('Swelling','Breathing Difficulty',)):
                              context.end_save_all_undo()
                              with knowledge_base.Gen_once if index == 5 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  total_prob_of_denominator =  context.lookup_data('val')
                                  with engine.lookup('facts', 'cond_probability', context, \
                                                     rule.foreach_patterns(6)) \
                                    as gen_6:
                                    for dummy in gen_6:
                                      if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                        conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                                  with knowledge_base.Gen_once if index == 7 \
                                           else engine.lookup('facts', 'probability', context,
                                                              rule.foreach_patterns(7)) \
                                    as gen_7:
                                    for dummy in gen_7:
                                      uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                      mark17 = context.mark(True)
                                      if rule.pattern(2).match_data(context, context,
                                              float(uncertanity) ):
                                        context.end_save_all_undo()
                                        engine.assert_('facts', 'diagnosed_decease',
                                                       (rule.pattern(3).as_data(context),
                                                        rule.pattern(2).as_data(context),
                                                        rule.pattern(4).as_data(context),)),
                                        rule.rule_base.num_fc_rules_triggered += 1
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark17)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark9)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark8)
  finally:
    context.done()

def allergic_treat_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'diagnosed_decease', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('epipenCode') in context.lookup_data('equipment'):
                  engine.assert_('facts', 'first_aid',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def allergic_treat_normal_alt(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'diagnosed_decease', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('epipenCode') not in context.lookup_data('equipment'):
                  engine.assert_('facts', 'first_aid',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack__diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack_diagnosis(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'symptom', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'issue_type_question', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'observed_symptoms', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            if context.lookup_data('painCode') in context.lookup_data('symptom') and context.lookup_data('breathingDiffucltyCode') in context.lookup_data('symptom'):
                              if context.lookup_data('sweatingCode') in context.lookup_data('symptom') and context.lookup_data('chestPainCode') in context.lookup_data('symptom') :
                                with knowledge_base.Gen_once if index == 6 \
                                         else engine.lookup('facts', 'cond_probability', context,
                                                            rule.foreach_patterns(6)) \
                                  as gen_6:
                                  for dummy in gen_6:
                                    engine.assert_('facts', 'diagnosed_decease',
                                                   (rule.pattern(0).as_data(context),
                                                    rule.pattern(1).as_data(context),
                                                    rule.pattern(2).as_data(context),)),
                                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack_treatement(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def heart_attack_treatement_alternative_one(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'equipment', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'diagnosed_decease', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('asprinCode') in context.lookup_data('equipment'):
                  engine.assert_('facts', 'first_aid',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def hyporthermia_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def hypothermia_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'activity', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'symptom', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'issue_type_question', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        with knowledge_base.Gen_once if index == 5 \
                                 else engine.lookup('questions', 'exposed_activity', context,
                                                    rule.foreach_patterns(5)) \
                          as gen_5:
                          for dummy in gen_5:
                            if context.lookup_data('coldExposureCode') in context.lookup_data('activites'):
                              with knowledge_base.Gen_once if index == 6 \
                                       else engine.lookup('questions', 'observed_symptoms', context,
                                                          rule.foreach_patterns(6)) \
                                as gen_6:
                                for dummy in gen_6:
                                  if context.lookup_data('shiveringCode') in context.lookup_data('symptom') and context.lookup_data('slurredSpeechCode') in context.lookup_data('symptom'):
                                    if context.lookup_data('confusionCode') in context.lookup_data('symptom'):
                                      with knowledge_base.Gen_once if index == 7 \
                                               else engine.lookup('facts', 'cond_probability', context,
                                                                  rule.foreach_patterns(7)) \
                                        as gen_7:
                                        for dummy in gen_7:
                                          engine.assert_('facts', 'diagnosed_decease',
                                                         (rule.pattern(0).as_data(context),
                                                          rule.pattern(1).as_data(context),
                                                          rule.pattern(2).as_data(context),)),
                                          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def hyporthermia_treat_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def choking_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def choking_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'issue_type_question', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'observed_symptoms', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    if context.lookup_data('breathingDifficultyCode') in context.lookup_data('symptom') and context.lookup_data('coughingCode') in context.lookup_data('symptom'):
                      total_prob_of_denominator = 1
                      conditional_prob_numerator_conditional_prob_val = 1
                      mark7 = context.mark(True)
                      if rule.pattern(0).match_data(context, context,
                              'Choking'):
                        context.end_save_all_undo()
                        mark8 = context.mark(True)
                        if rule.pattern(1).match_data(context, context,
                                ('Coughing','Breathing Difficulty',)):
                          context.end_save_all_undo()
                          with knowledge_base.Gen_once if index == 4 \
                                   else engine.lookup('facts', 'probability', context,
                                                      rule.foreach_patterns(4)) \
                            as gen_4:
                            for dummy in gen_4:
                              total_prob_of_denominator =  context.lookup_data('val')
                              with engine.lookup('facts', 'cond_probability', context, \
                                                 rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                    conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                              with knowledge_base.Gen_once if index == 6 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(6)) \
                                as gen_6:
                                for dummy in gen_6:
                                  uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                  mark16 = context.mark(True)
                                  if rule.pattern(2).match_data(context, context,
                                          float(uncertanity)         ):
                                    context.end_save_all_undo()
                                    engine.assert_('facts', 'diagnosed_decease',
                                                   (rule.pattern(3).as_data(context),
                                                    rule.pattern(2).as_data(context),
                                                    rule.pattern(4).as_data(context),)),
                                    rule.rule_base.num_fc_rules_triggered += 1
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark16)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark8)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark7)
  finally:
    context.done()

def choking_treat_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def choking_treat_alt(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def snake_bite_diagnosis_heuristic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('questions', 'issue_type_question', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('facts', 'diagnosed_decease',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def snake_bite_diagnosis_normal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'symptom', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'symptom', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('facts', 'symptom', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('questions', 'issue_type_question', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    with knowledge_base.Gen_once if index == 4 \
                             else engine.lookup('questions', 'observed_symptoms', context,
                                                rule.foreach_patterns(4)) \
                      as gen_4:
                      for dummy in gen_4:
                        if context.lookup_data('punctureCode') in context.lookup_data('symptom') and context.lookup_data('swellingCode') in context.lookup_data('symptom') and context.lookup_data('discolorationCode') in context.lookup_data('symptom'):
                          total_prob_of_denominator = 1
                          conditional_prob_numerator_conditional_prob_val = 1
                          mark8 = context.mark(True)
                          if rule.pattern(0).match_data(context, context,
                                  'Snake Bite'):
                            context.end_save_all_undo()
                            mark9 = context.mark(True)
                            if rule.pattern(1).match_data(context, context,
                                    ('Puncture Wound','Swelling','Discoloration',)):
                              context.end_save_all_undo()
                              with knowledge_base.Gen_once if index == 5 \
                                       else engine.lookup('facts', 'probability', context,
                                                          rule.foreach_patterns(5)) \
                                as gen_5:
                                for dummy in gen_5:
                                  total_prob_of_denominator =  context.lookup_data('val')
                                  with engine.lookup('facts', 'cond_probability', context, \
                                                     rule.foreach_patterns(6)) \
                                    as gen_6:
                                    for dummy in gen_6:
                                      if context.lookup_data('given_symptom_name') in context.lookup_data('given_symptoms_list'):
                                        conditional_prob_numerator_conditional_prob_val = conditional_prob_numerator_conditional_prob_val * context.lookup_data('val2')
                                  with knowledge_base.Gen_once if index == 7 \
                                           else engine.lookup('facts', 'probability', context,
                                                              rule.foreach_patterns(7)) \
                                    as gen_7:
                                    for dummy in gen_7:
                                      uncertanity  = float(context.lookup_data('issue_prob')*conditional_prob_numerator_conditional_prob_val)/total_prob_of_denominator
                                      mark17 = context.mark(True)
                                      if rule.pattern(2).match_data(context, context,
                                              float(uncertanity) ):
                                        context.end_save_all_undo()
                                        engine.assert_('facts', 'diagnosed_decease',
                                                       (rule.pattern(3).as_data(context),
                                                        rule.pattern(2).as_data(context),
                                                        rule.pattern(4).as_data(context),)),
                                        rule.rule_base.num_fc_rules_triggered += 1
                                      else: context.end_save_all_undo()
                                      context.undo_to_mark(mark17)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark9)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark8)
  finally:
    context.done()

def snake_bite_treat(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('elasticBandageCode') in context.lookup_data('equipment'):
                  engine.assert_('facts', 'first_aid',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def snake_bite_treat_alt_one(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                if context.lookup_data('icePackCode') in context.lookup_data('equipment'):
                  engine.assert_('facts', 'first_aid',
                                 (rule.pattern(0).as_data(context),
                                  rule.pattern(1).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def snake_bite_treat_alt_two(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'first_aid',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def find_missing_equipment(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'diagnosed_decease', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'issue_to_equipment', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'first_aid_equipment', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                required_equipments_code_list = []
                with engine.lookup('facts', 'issue_to_equipment', context, \
                                   rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    required_equipments_code_list.append(context.lookup_data('required_equipments_code'))
                having_equipments = []
                with engine.lookup('facts', 'equipment', context, \
                                   rule.foreach_patterns(4)) \
                  as gen_4:
                  for dummy in gen_4:
                    if context.lookup_data('equipmentCode') in context.lookup_data('having_equipments_code_list'):
                      having_equipments.append(context.lookup_data('equipment'))
                required_equipment_list = []
                with engine.lookup('facts', 'equipment', context, \
                                   rule.foreach_patterns(5)) \
                  as gen_5:
                  for dummy in gen_5:
                    if context.lookup_data('equipmentCode') in required_equipments_code_list:
                      required_equipment_list.append(context.lookup_data('equipment'))
                missing_equip_list = [item for item in required_equipment_list if item not in having_equipments]
                mark15 = context.mark(True)
                if rule.pattern(0).match_data(context, context,
                        list(missing_equip_list)):
                  context.end_save_all_undo()
                  engine.assert_('facts', 'missing_equipment',
                                 (rule.pattern(1).as_data(context),
                                  rule.pattern(0).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
                else: context.end_save_all_undo()
                context.undo_to_mark(mark15)
  finally:
    context.done()

def outdoor_cut_guidance(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'location_to_code', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'current_location', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'diagnosed_decease', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('facts', 'location_advice',
                                   (rule.pattern(0).as_data(context),
                                    rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def workplace_burn_guidance(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'location_to_code', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'current_location', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'diagnosed_decease', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('facts', 'location_advice',
                                   (rule.pattern(0).as_data(context),
                                    rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def wilderness_fracture_guidance(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'issue', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts', 'location_to_code', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('questions', 'current_location', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('facts', 'diagnosed_decease', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('facts', 'location_advice',
                                   (rule.pattern(0).as_data(context),
                                    rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc')
  
  fc_rule.fc_rule('cut_diagnosis_heuristic', This_rule_base, cut_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Cut'),
       contexts.variable('cutCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('cutCode'),),
      False),),
    (pattern.pattern_literal('Cut'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('cut_diagnosis_normal', This_rule_base, cut_diagnosis_normal,
    (('facts', 'symptom',
      (pattern.pattern_literal('Bleeding'),
       contexts.variable('bleedingCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Cut'),
     pattern.pattern_literal('Since bleeding is occuring, there is a high probability to be a cut somewhere in the body.'),))
  
  fc_rule.fc_rule('cut_treat', This_rule_base, cut_treat,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Cut'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Bandages'),
       contexts.variable('bandagesCode'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Antiseptic'),
       contexts.variable('AntisepticCode'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Cut'),
     pattern.pattern_literal("Clean the wound, apply antiseptic, and bandage it to stop bleeding."),))
  
  fc_rule.fc_rule('burn_diagnosis_heuristic', This_rule_base, burn_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Burn'),
       contexts.variable('burnCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('burnCode'),),
      False),),
    (pattern.pattern_literal('Burn'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('burn_diagnosis_normal', This_rule_base, burn_diagnosis_normal,
    (('facts', 'symptom',
      (pattern.pattern_literal('Burning Sensation'),
       contexts.variable('burningSensationCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Burn'),
     pattern.pattern_literal('Because a burning sensatiton implies that the body was exposed to some unencessary heat.'),))
  
  fc_rule.fc_rule('burn_treat', This_rule_base, burn_treat,
    (('facts', 'equipment',
      (pattern.pattern_literal('Water'),
       contexts.variable('waterCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Burn'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Burn'),
     pattern.pattern_literal("Cool the burn under running water for 10 minutes and cover with a sterile dressing."),))
  
  fc_rule.fc_rule('burn_treat_alternative', This_rule_base, burn_treat_alternative,
    (('facts', 'equipment',
      (pattern.pattern_literal('Dry Cloth'),
       contexts.variable('dryClothCode'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Non-stick gauze pad'),
       contexts.variable('nonStickGauzeCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Burn'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Burn'),
     pattern.pattern_literal('Cover the burn with a clean, dry cloth (or a non-stick gauze pad). Avoid using  ointments on severe burns to prevent shock. Keep the person warm and calm while waiting for emergency services.'),))
  
  fc_rule.fc_rule('fracture_diagnosis_heuristic', This_rule_base, fracture_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Fracture'),
       contexts.variable('fractureCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('fractureCode'),),
      False),),
    (pattern.pattern_literal('Fracture'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('fracture_diagnosis_normal_one', This_rule_base, fracture_diagnosis_normal_one,
    (('facts', 'symptom',
      (pattern.pattern_literal('Swelling'),
       contexts.variable('swellingCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Pain'),
       contexts.variable('painCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Deformity'),
       contexts.variable('deformityCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Fracture'),
     pattern.pattern_literal('This diagnosis was made because the observed symptoms of swelling, pain, and deformity strongly suggest a fracture based on their conditional probabilities.'),))
  
  fc_rule.fc_rule('fracture_diagnosis_normal_two', This_rule_base, fracture_diagnosis_normal_two,
    (('facts', 'symptom',
      (pattern.pattern_literal('Swelling'),
       contexts.variable('swellingCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Pain'),
       contexts.variable('painCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Deformity'),
       contexts.variable('deformityCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Fracture'),
     pattern.pattern_literal('This diagnosis was made because the observed symptoms of swelling and bruising are commonly associated with fractures, as indicated by their conditional probabilities.'),))
  
  fc_rule.fc_rule('fracture_treat_1', This_rule_base, fracture_treat_1,
    (('facts', 'equipment',
      (pattern.pattern_literal('Splint'),
       contexts.variable('splintCode'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Ice Pack'),
       contexts.variable('icePackCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Fracture'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Fracture'),
     pattern.pattern_literal("Immobilize the limb using a splint and seek medical help immediately. Try to find an ice pack and apply to reduce swelling"),))
  
  fc_rule.fc_rule('fracture_treat_two', This_rule_base, fracture_treat_two,
    (('facts', 'equipment',
      (pattern.pattern_literal('Splint'),
       contexts.variable('splintCode'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Ice Pack'),
       contexts.variable('icePackCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Fracture'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Fracture'),
     pattern.pattern_literal("Immobilize the area using a splint, apply an ice pack to reduce swelling, and seek medical attention."),))
  
  fc_rule.fc_rule('shock_diagnosis_heuristic', This_rule_base, shock_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Shock'),
       contexts.variable('shockCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('shockCode'),),
      False),),
    (pattern.pattern_literal('Shock'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('shock_diagnosis_normal', This_rule_base, shock_diagnosis_normal,
    (('facts', 'symptom',
      (pattern.pattern_literal('Dizziness'),
       contexts.variable('dizzinessCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Weak Pulse'),
       contexts.variable('weak_pulseCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Shock'),
     pattern.pattern_literal('Due to the patient having Dizziness followed by Weak pulse it is a high likelihood that the patient is suffering from a shock.'),))
  
  fc_rule.fc_rule('shock_treat', This_rule_base, shock_treat,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Shock'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Shock'),
     pattern.pattern_literal("Lay the person down, keep them warm, and elevate their legs if possible."),))
  
  fc_rule.fc_rule('concussion_diagnosis_heuristic', This_rule_base, concussion_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Concussion'),
       contexts.variable('concussionCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('concussionCode'),),
      False),),
    (pattern.pattern_literal('Concussion'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('concussion_diagnosis_normal_one', This_rule_base, concussion_diagnosis_normal_one,
    (('facts', 'activity',
      (pattern.pattern_literal('Head injury'),
       contexts.variable('headInjuryCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Confusion'),
       contexts.variable('confusionCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Headache'),
       contexts.variable('headacheCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Nausea'),
       contexts.variable('nauseaCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('questions', 'exposed_activity',
      (contexts.variable('activity'),),
      False),
     ('facts', 'cond_probability',
      (pattern.pattern_literal('Concussion'),
       pattern.pattern_literal(('Head injury', 'Confusion', 'Headache', 'Nausea',)),
       contexts.variable('uncertanity'),),
      False),),
    (pattern.pattern_literal('Concussion'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Because the patient had an Head injury and shoecases symptoms like confusion, headache and Nause'),))
  
  fc_rule.fc_rule('concussion_diagnosis_normal_two', This_rule_base, concussion_diagnosis_normal_two,
    (('facts', 'activity',
      (pattern.pattern_literal('No idea'),
       contexts.variable('noIdeaInjuryCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Confusion'),
       contexts.variable('confusionCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Headache'),
       contexts.variable('headacheCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Nausea'),
       contexts.variable('nauseaCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('questions', 'exposed_activity',
      (contexts.variable('activity'),),
      False),
     ('facts', 'cond_probability',
      (pattern.pattern_literal('Concussion'),
       pattern.pattern_literal(('Confusion', 'Headache', 'Nausea',)),
       contexts.variable('uncertanity'),),
      False),),
    (pattern.pattern_literal('Concussion'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Even though you are not sure about patients head injury, still due to showcasing of symptoms like confusion, headache and Nausea, concussion might be the case.'),))
  
  fc_rule.fc_rule('concussion_diagnosis_normal_three', This_rule_base, concussion_diagnosis_normal_three,
    (('facts', 'activity',
      (pattern.pattern_literal('Head injury'),
       contexts.variable('headInjuryCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Confusion'),
       contexts.variable('confusionCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Headache'),
       contexts.variable('headacheCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Nausea'),
       contexts.variable('nauseaCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'exposed_activity',
      (contexts.variable('activity'),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'cond_probability',
      (pattern.pattern_literal('Concussion'),
       pattern.pattern_literal(('Head injury', 'Confusion', 'Headache',)),
       contexts.variable('uncertanity'),),
      False),),
    (pattern.pattern_literal('Concussion'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Because the patient had an Head injury and shoecases symptoms like confusion and headache'),))
  
  fc_rule.fc_rule('concussion_treat_normal', This_rule_base, concussion_treat_normal,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Concussion'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Concussion'),
     pattern.pattern_literal("Keep the person awake, avoid giving food and drink and seek medical attention immediately."),))
  
  fc_rule.fc_rule('bee_sting_diagnosis_heuristic', This_rule_base, bee_sting_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Bee Sting'),
       contexts.variable('beeStingCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('beeStingCode'),),
      False),),
    (pattern.pattern_literal('Bee Sting'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('bee_sting_diagnosis_normal', This_rule_base, bee_sting_diagnosis_normal,
    (('facts', 'symptom',
      (pattern.pattern_literal('Swelling'),
       contexts.variable('swellingCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Pain'),
       contexts.variable('painCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Bee Sting'),
     pattern.pattern_literal('Because the patient showcases the symptoms of Swelling followed by pain'),))
  
  fc_rule.fc_rule('bee_sting_treat', This_rule_base, bee_sting_treat,
    (('facts', 'equipment',
      (pattern.pattern_literal('Ice Pack'),
       contexts.variable('icePackCode'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Antihistamine'),
       contexts.variable('antihistamineCode'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Bee Sting'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Bee Sting'),
     pattern.pattern_literal("Remove the stinger, apply an ice pack to reduce swelling, and take an antihistamine if needed."),))
  
  fc_rule.fc_rule('allergic_diagnosis_heuristic', This_rule_base, allergic_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Allergy'),
       contexts.variable('allergyCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('allergyCode'),),
      False),),
    (pattern.pattern_literal('Allergy'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('allergic_diagnosis_normal_one', This_rule_base, allergic_diagnosis_normal_one,
    (('facts', 'symptom',
      (pattern.pattern_literal('Swelling'),
       contexts.variable('swellingCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Breathing Difficulty'),
       contexts.variable('breathingDifficultyCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Chest Pain'),
       contexts.variable('chestPainCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Allergy'),
     pattern.pattern_literal('Because the patient is showcasing Swelings followed by breathing difficulty and heart pain'),))
  
  fc_rule.fc_rule('allergic_diagnosis_normal_two', This_rule_base, allergic_diagnosis_normal_two,
    (('facts', 'symptom',
      (pattern.pattern_literal('Swelling'),
       contexts.variable('swellingCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Breathing Difficulty'),
       contexts.variable('breathingDifficultyCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Chest Pain'),
       contexts.variable('chestPainCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Allergy'),
     pattern.pattern_literal('Because the patient is showcasing Swelings followed by breathing difficulty'),))
  
  fc_rule.fc_rule('allergic_treat_normal', This_rule_base, allergic_treat_normal,
    (('facts', 'equipment',
      (pattern.pattern_literal('EpiPen'),
       contexts.variable('epipenCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Allergy'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Allergy'),
     pattern.pattern_literal("Administer epinephrine via an EpiPen and seek emergency medical help."),))
  
  fc_rule.fc_rule('allergic_treat_normal_alt', This_rule_base, allergic_treat_normal_alt,
    (('facts', 'equipment',
      (pattern.pattern_literal('EpiPen'),
       contexts.variable('epipenCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Allergy'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Allergy'),
     pattern.pattern_literal("If an EpiPen isn’t available or expired, remove the person from the allergen source immediately. Encourage them to remain calm and still to reduce the spread of the reaction while contacting emergency services."),))
  
  fc_rule.fc_rule('heart_attack__diagnosis_heuristic', This_rule_base, heart_attack__diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Heart Attack'),
       contexts.variable('heartAttackCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('heartAttackCode'),),
      False),),
    (pattern.pattern_literal('Heart Attack'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('heart_attack_diagnosis', This_rule_base, heart_attack_diagnosis,
    (('facts', 'symptom',
      (pattern.pattern_literal('Chest Pain'),
       contexts.variable('chestPainCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Pain'),
       contexts.variable('painCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Breathing Difficulty'),
       contexts.variable('breathingDiffucltyCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Sweating'),
       contexts.variable('sweatingCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'cond_probability',
      (pattern.pattern_literal('Heart Attack'),
       pattern.pattern_literal(('Chest Pain', 'Pain', 'Breathing Difficulty', 'Sweating',)),
       contexts.variable('uncertanity'),),
      False),),
    (pattern.pattern_literal('Heart Attack'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Because Chest pain followed by Shortness of Breath and sweating are major symptoms of a heart attack'),))
  
  fc_rule.fc_rule('heart_attack_treatement', This_rule_base, heart_attack_treatement,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Heart Attack'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Heart Attack'),
     pattern.pattern_literal("Call emergency services and keep the person calm."),))
  
  fc_rule.fc_rule('heart_attack_treatement_alternative_one', This_rule_base, heart_attack_treatement_alternative_one,
    (('facts', 'equipment',
      (pattern.pattern_literal('Asprin'),
       contexts.variable('asprinCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Heart Attack'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Heart Attack'),
     pattern.pattern_literal("Call emergency services immediately. Loosen tight clothing, and if they are conscious and not allergic, offer aspirin to chew while waiting for help. Do not allow them to eat or drink. Monitor their breathing and pulse."),))
  
  fc_rule.fc_rule('hyporthermia_diagnosis_heuristic', This_rule_base, hyporthermia_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Hypothermia'),
       contexts.variable('hypothermiaCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('hypothermiaCode'),),
      False),),
    (pattern.pattern_literal('Hypothermia'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('hypothermia_diagnosis_normal', This_rule_base, hypothermia_diagnosis_normal,
    (('facts', 'activity',
      (pattern.pattern_literal('Cold exposure'),
       contexts.variable('coldExposureCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Shivering'),
       contexts.variable('shiveringCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Slurred Speech'),
       contexts.variable('slurredSpeechCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Confusion'),
       contexts.variable('confusionCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'exposed_activity',
      (contexts.variable('activites'),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'cond_probability',
      (pattern.pattern_literal('Hypothermia'),
       pattern.pattern_literal(('Cold exposure', 'Shivering', 'Slurred Speech', 'Confusion',)),
       contexts.variable('uncertanity'),),
      False),),
    (pattern.pattern_literal('Hypothermia'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Because the patient who was experienced some cold exposure is showcasing symptoms like Shivering, slurred speech and confusion.'),))
  
  fc_rule.fc_rule('hyporthermia_treat_normal', This_rule_base, hyporthermia_treat_normal,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Hypothermia'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Hypothermia'),
     pattern.pattern_literal("Wrap the person in layers of available clothing, focusing on their head and neck. Use body heat if necessary by staying close. Avoid applying external heat sources directly to prevent shock."),))
  
  fc_rule.fc_rule('choking_diagnosis_heuristic', This_rule_base, choking_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Choking'),
       contexts.variable('chokingCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('chokingCode'),),
      False),),
    (pattern.pattern_literal('Choking'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('choking_diagnosis_normal', This_rule_base, choking_diagnosis_normal,
    (('facts', 'symptom',
      (pattern.pattern_literal('Breathing Difficulty'),
       contexts.variable('breathingDifficultyCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Coughing'),
       contexts.variable('coughingCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Choking'),
     pattern.pattern_literal('Because the patient is Coughing and showing breathing diffculties'),))
  
  fc_rule.fc_rule('choking_treat_normal', This_rule_base, choking_treat_normal,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Choking'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Choking'),
     pattern.pattern_literal("Perform the Heimlich maneuver and seek emergency medical help if the obstruction is not cleared."),))
  
  fc_rule.fc_rule('choking_treat_alt', This_rule_base, choking_treat_alt,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Choking'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Choking'),
     pattern.pattern_literal("lean the person forward and firmly strike their back between the shoulder blades with the palm of your hand. Repeat up to five times or until the object is expelled."),))
  
  fc_rule.fc_rule('snake_bite_diagnosis_heuristic', This_rule_base, snake_bite_diagnosis_heuristic,
    (('facts', 'issue',
      (pattern.pattern_literal('Snake Bite'),
       contexts.variable('snakeBiteCode'),),
      False),
     ('questions', 'issue_type_question',
      (contexts.variable('snakeBiteCode'),),
      False),),
    (pattern.pattern_literal('Snake Bite'),
     pattern.pattern_literal(1),
     pattern.pattern_literal(" "),))
  
  fc_rule.fc_rule('snake_bite_diagnosis_normal', This_rule_base, snake_bite_diagnosis_normal,
    (('facts', 'symptom',
      (pattern.pattern_literal('Puncture Wound'),
       contexts.variable('punctureCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Swelling'),
       contexts.variable('swellingCode'),),
      False),
     ('facts', 'symptom',
      (pattern.pattern_literal('Discoloration'),
       contexts.variable('discolorationCode'),),
      False),
     ('questions', 'issue_type_question',
      (pattern.pattern_literal(1),),
      False),
     ('questions', 'observed_symptoms',
      (contexts.variable('symptom'),),
      False),
     ('facts', 'probability',
      (contexts.variable('given_symptoms_list'),
       contexts.variable('val'),),
      False),
     ('facts', 'cond_probability',
      (contexts.variable('given_symptom_name'),
       contexts.variable('issue'),
       contexts.variable('val2'),),
      True),
     ('facts', 'probability',
      (contexts.variable('issue'),
       contexts.variable('issue_prob'),),
      False),),
    (contexts.variable('issue'),
     contexts.variable('given_symptoms_list'),
     contexts.variable('uncertanity'),
     pattern.pattern_literal('Snake Bite'),
     pattern.pattern_literal('Because the patient has a puncure wound, swellings and  discoloration'),))
  
  fc_rule.fc_rule('snake_bite_treat', This_rule_base, snake_bite_treat,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Snake Bite'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Elastic Bandage'),
       contexts.variable('elasticBandageCode'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Snake Bite'),
     pattern.pattern_literal("Keep the bite area immobilized below heart level, apply a loose elastic bandage above the bite to slow venom spread, and seek immediate medical help."),))
  
  fc_rule.fc_rule('snake_bite_treat_alt_one', This_rule_base, snake_bite_treat_alt_one,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Snake Bite'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('facts', 'equipment',
      (pattern.pattern_literal('Ice Pack'),
       contexts.variable('icePackCode'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('equipment'),),
      False),),
    (pattern.pattern_literal('Snake Bite'),
     pattern.pattern_literal("AVOID applying ice or suctioning venom. Focus on keeping the person calm while awaiting medical help"),))
  
  fc_rule.fc_rule('snake_bite_treat_alt_two', This_rule_base, snake_bite_treat_alt_two,
    (('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Snake Bite'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Snake Bite'),
     pattern.pattern_literal("Keep the person as still as possible, and use any available materials to create a sling to immobilize the affected limb."),))
  
  fc_rule.fc_rule('find_missing_equipment', This_rule_base, find_missing_equipment,
    (('facts', 'diagnosed_decease',
      (contexts.variable('issue'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('facts', 'issue_to_equipment',
      (contexts.variable('issue'),
       contexts.variable('required_equipments_code_list'),),
      False),
     ('questions', 'first_aid_equipment',
      (contexts.variable('having_equipments_code_list'),),
      False),
     ('facts', 'issue_to_equipment',
      (contexts.variable('issue'),
       contexts.variable('required_equipments_code'),),
      True),
     ('facts', 'equipment',
      (contexts.variable('equipment'),
       contexts.variable('equipmentCode'),),
      True),
     ('facts', 'equipment',
      (contexts.variable('equipment'),
       contexts.variable('equipmentCode'),),
      True),),
    (contexts.variable('missing_equip_list'),
     contexts.variable('issue'),))
  
  fc_rule.fc_rule('outdoor_cut_guidance', This_rule_base, outdoor_cut_guidance,
    (('facts', 'issue',
      (pattern.pattern_literal('Cut'),
       contexts.variable('cutCode'),),
      False),
     ('facts', 'location_to_code',
      (pattern.pattern_literal('Outdoor'),
       contexts.variable('outdoorCode'),),
      False),
     ('questions', 'current_location',
      (contexts.variable('outdoorCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Cut'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Cut'),
     pattern.pattern_literal("In outdoor locations, ensure the area is safe from further injury sources and sanitize hands if possible before administering first aid."),))
  
  fc_rule.fc_rule('workplace_burn_guidance', This_rule_base, workplace_burn_guidance,
    (('facts', 'issue',
      (pattern.pattern_literal('Burn'),
       contexts.variable('burnCode'),),
      False),
     ('facts', 'location_to_code',
      (pattern.pattern_literal('Workplace'),
       contexts.variable('workplaceCode'),),
      False),
     ('questions', 'current_location',
      (pattern.pattern_literal(3),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Burn'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Burn'),
     pattern.pattern_literal("In the workplace, assess any surrounding hazards, and contact the onsite medical team if available."),))
  
  fc_rule.fc_rule('wilderness_fracture_guidance', This_rule_base, wilderness_fracture_guidance,
    (('facts', 'issue',
      (pattern.pattern_literal('Fracture'),
       contexts.variable('fractureCode'),),
      False),
     ('facts', 'location_to_code',
      (pattern.pattern_literal('Wilderness'),
       contexts.variable('wildernessCode'),),
      False),
     ('questions', 'current_location',
      (contexts.variable('wildernessCode'),),
      False),
     ('facts', 'diagnosed_decease',
      (pattern.pattern_literal('Fracture'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (pattern.pattern_literal('Fracture'),
     pattern.pattern_literal("In wilderness settings, prioritize stabilization and signaling for help. Use available materials like tree branches or hiking poles as improvised splints. Minimize movement to prevent further injury."),))


Krb_filename = '..\\fc.krb'
Krb_lineno_map = (
    ((12, 16), (7, 7)),
    ((17, 21), (8, 8)),
    ((22, 25), (11, 11)),
    ((34, 38), (18, 18)),
    ((39, 43), (20, 20)),
    ((44, 48), (21, 21)),
    ((49, 49), (22, 22)),
    ((50, 50), (25, 25)),
    ((51, 51), (26, 26)),
    ((54, 54), (28, 28)),
    ((58, 58), (29, 29)),
    ((60, 64), (31, 31)),
    ((65, 65), (32, 32)),
    ((66, 69), (35, 35)),
    ((70, 70), (36, 36)),
    ((71, 71), (37, 37)),
    ((72, 76), (39, 39)),
    ((77, 77), (41, 41)),
    ((80, 80), (42, 42)),
    ((82, 85), (45, 45)),
    ((100, 104), (51, 51)),
    ((105, 109), (52, 52)),
    ((110, 114), (53, 53)),
    ((115, 119), (55, 55)),
    ((120, 120), (56, 56)),
    ((121, 123), (59, 59)),
    ((132, 136), (68, 68)),
    ((137, 141), (69, 69)),
    ((142, 145), (72, 72)),
    ((154, 158), (78, 78)),
    ((159, 163), (80, 80)),
    ((164, 168), (81, 81)),
    ((169, 169), (82, 82)),
    ((170, 170), (86, 86)),
    ((171, 171), (87, 87)),
    ((174, 174), (89, 89)),
    ((178, 178), (90, 90)),
    ((180, 184), (92, 92)),
    ((185, 185), (93, 93)),
    ((186, 189), (97, 97)),
    ((190, 190), (98, 98)),
    ((191, 191), (99, 99)),
    ((192, 196), (101, 101)),
    ((197, 197), (103, 103)),
    ((200, 200), (104, 104)),
    ((202, 205), (108, 108)),
    ((220, 224), (113, 113)),
    ((225, 229), (115, 115)),
    ((230, 234), (117, 117)),
    ((235, 235), (118, 118)),
    ((236, 238), (121, 121)),
    ((247, 251), (126, 126)),
    ((252, 256), (127, 127)),
    ((257, 261), (129, 129)),
    ((262, 266), (131, 131)),
    ((267, 267), (132, 132)),
    ((268, 270), (135, 135)),
    ((279, 283), (141, 141)),
    ((284, 288), (142, 142)),
    ((289, 292), (145, 145)),
    ((301, 305), (151, 151)),
    ((306, 310), (152, 152)),
    ((311, 315), (153, 153)),
    ((316, 320), (155, 155)),
    ((321, 325), (157, 157)),
    ((326, 326), (158, 158)),
    ((327, 327), (162, 162)),
    ((328, 328), (163, 163)),
    ((331, 331), (165, 165)),
    ((335, 335), (166, 166)),
    ((337, 341), (168, 168)),
    ((342, 342), (169, 169)),
    ((343, 346), (172, 172)),
    ((347, 347), (173, 173)),
    ((348, 348), (174, 174)),
    ((349, 353), (176, 176)),
    ((354, 354), (178, 178)),
    ((357, 357), (179, 179)),
    ((359, 362), (181, 181)),
    ((377, 381), (186, 186)),
    ((382, 386), (187, 187)),
    ((387, 391), (188, 188)),
    ((392, 396), (190, 190)),
    ((397, 401), (192, 192)),
    ((402, 402), (193, 193)),
    ((403, 403), (197, 197)),
    ((404, 404), (198, 198)),
    ((407, 407), (200, 200)),
    ((411, 411), (201, 201)),
    ((413, 417), (203, 203)),
    ((418, 418), (204, 204)),
    ((419, 422), (207, 207)),
    ((423, 423), (208, 208)),
    ((424, 424), (209, 209)),
    ((425, 429), (211, 211)),
    ((430, 430), (213, 213)),
    ((433, 433), (214, 214)),
    ((435, 438), (217, 217)),
    ((453, 457), (221, 221)),
    ((458, 462), (222, 222)),
    ((463, 467), (224, 224)),
    ((468, 472), (226, 226)),
    ((473, 473), (227, 227)),
    ((474, 476), (230, 230)),
    ((485, 489), (235, 235)),
    ((490, 494), (236, 236)),
    ((495, 499), (238, 238)),
    ((500, 504), (240, 240)),
    ((505, 505), (241, 241)),
    ((506, 506), (242, 242)),
    ((507, 509), (245, 245)),
    ((518, 522), (252, 252)),
    ((523, 527), (253, 253)),
    ((528, 531), (256, 256)),
    ((540, 544), (262, 262)),
    ((545, 549), (263, 263)),
    ((550, 554), (265, 265)),
    ((555, 559), (266, 266)),
    ((560, 560), (267, 267)),
    ((561, 561), (271, 271)),
    ((562, 562), (272, 272)),
    ((565, 565), (274, 274)),
    ((569, 569), (275, 275)),
    ((571, 575), (277, 277)),
    ((576, 576), (278, 278)),
    ((577, 580), (281, 281)),
    ((581, 581), (282, 282)),
    ((582, 582), (283, 283)),
    ((583, 587), (285, 285)),
    ((588, 588), (287, 287)),
    ((591, 591), (288, 288)),
    ((593, 596), (290, 290)),
    ((611, 615), (295, 295)),
    ((616, 618), (298, 298)),
    ((627, 631), (305, 305)),
    ((632, 636), (306, 306)),
    ((637, 640), (309, 309)),
    ((649, 653), (313, 313)),
    ((654, 658), (314, 314)),
    ((659, 663), (315, 315)),
    ((664, 668), (316, 316)),
    ((669, 673), (318, 318)),
    ((674, 678), (320, 320)),
    ((679, 679), (321, 321)),
    ((680, 680), (322, 322)),
    ((681, 685), (324, 324)),
    ((686, 686), (325, 325)),
    ((687, 691), (327, 327)),
    ((692, 695), (331, 331)),
    ((704, 708), (336, 336)),
    ((709, 713), (337, 337)),
    ((714, 718), (338, 338)),
    ((719, 723), (339, 339)),
    ((724, 728), (342, 342)),
    ((729, 733), (345, 345)),
    ((734, 734), (346, 346)),
    ((735, 735), (347, 347)),
    ((736, 740), (349, 349)),
    ((741, 741), (350, 350)),
    ((742, 746), (352, 352)),
    ((747, 750), (354, 354)),
    ((759, 763), (359, 359)),
    ((764, 768), (360, 360)),
    ((769, 773), (361, 361)),
    ((774, 778), (362, 362)),
    ((779, 783), (364, 364)),
    ((784, 788), (366, 366)),
    ((789, 789), (367, 367)),
    ((790, 794), (369, 369)),
    ((795, 795), (370, 370)),
    ((796, 800), (372, 372)),
    ((801, 804), (375, 375)),
    ((813, 817), (380, 380)),
    ((818, 820), (383, 383)),
    ((829, 833), (389, 389)),
    ((834, 838), (390, 390)),
    ((839, 842), (393, 393)),
    ((851, 855), (397, 397)),
    ((856, 860), (398, 398)),
    ((861, 865), (400, 400)),
    ((866, 870), (402, 402)),
    ((871, 871), (403, 403)),
    ((872, 872), (407, 407)),
    ((873, 873), (408, 408)),
    ((876, 876), (410, 410)),
    ((880, 880), (411, 411)),
    ((882, 886), (413, 413)),
    ((887, 887), (414, 414)),
    ((888, 891), (417, 417)),
    ((892, 892), (418, 418)),
    ((893, 893), (419, 419)),
    ((894, 898), (421, 421)),
    ((899, 899), (423, 423)),
    ((902, 902), (424, 424)),
    ((904, 907), (427, 427)),
    ((922, 926), (432, 432)),
    ((927, 931), (433, 433)),
    ((932, 936), (435, 435)),
    ((937, 937), (436, 436)),
    ((938, 942), (438, 438)),
    ((943, 945), (441, 441)),
    ((954, 958), (449, 449)),
    ((959, 963), (450, 450)),
    ((964, 967), (453, 453)),
    ((976, 980), (457, 457)),
    ((981, 985), (458, 458)),
    ((986, 990), (459, 459)),
    ((991, 995), (462, 462)),
    ((996, 1000), (464, 464)),
    ((1001, 1001), (465, 465)),
    ((1002, 1002), (469, 469)),
    ((1003, 1003), (470, 470)),
    ((1006, 1006), (472, 472)),
    ((1010, 1010), (473, 473)),
    ((1012, 1016), (475, 475)),
    ((1017, 1017), (476, 476)),
    ((1018, 1021), (479, 479)),
    ((1022, 1022), (480, 480)),
    ((1023, 1023), (481, 481)),
    ((1024, 1028), (483, 483)),
    ((1029, 1029), (485, 485)),
    ((1032, 1032), (486, 486)),
    ((1034, 1037), (489, 489)),
    ((1052, 1056), (493, 493)),
    ((1057, 1061), (494, 494)),
    ((1062, 1066), (495, 495)),
    ((1067, 1071), (497, 497)),
    ((1072, 1076), (499, 499)),
    ((1077, 1077), (500, 500)),
    ((1078, 1078), (504, 504)),
    ((1079, 1079), (505, 505)),
    ((1082, 1082), (507, 507)),
    ((1086, 1086), (508, 508)),
    ((1088, 1092), (510, 510)),
    ((1093, 1093), (511, 511)),
    ((1094, 1097), (514, 514)),
    ((1098, 1098), (515, 515)),
    ((1099, 1099), (516, 516)),
    ((1100, 1104), (518, 518)),
    ((1105, 1105), (520, 520)),
    ((1108, 1108), (521, 521)),
    ((1110, 1113), (524, 524)),
    ((1128, 1132), (528, 528)),
    ((1133, 1137), (530, 530)),
    ((1138, 1142), (532, 532)),
    ((1143, 1143), (533, 533)),
    ((1144, 1146), (536, 536)),
    ((1155, 1159), (540, 540)),
    ((1160, 1164), (542, 542)),
    ((1165, 1169), (544, 544)),
    ((1170, 1170), (545, 545)),
    ((1171, 1173), (548, 548)),
    ((1182, 1186), (556, 556)),
    ((1187, 1191), (557, 557)),
    ((1192, 1195), (561, 561)),
    ((1204, 1208), (565, 565)),
    ((1209, 1213), (566, 566)),
    ((1214, 1218), (567, 567)),
    ((1219, 1223), (568, 568)),
    ((1224, 1228), (570, 570)),
    ((1229, 1233), (572, 572)),
    ((1234, 1234), (573, 573)),
    ((1235, 1235), (574, 574)),
    ((1236, 1240), (576, 576)),
    ((1241, 1244), (578, 578)),
    ((1253, 1257), (584, 584)),
    ((1258, 1260), (587, 587)),
    ((1269, 1273), (592, 592)),
    ((1274, 1278), (593, 593)),
    ((1279, 1283), (595, 595)),
    ((1284, 1284), (596, 596)),
    ((1285, 1287), (599, 599)),
    ((1296, 1300), (607, 607)),
    ((1301, 1305), (608, 608)),
    ((1306, 1309), (612, 612)),
    ((1318, 1322), (616, 616)),
    ((1323, 1327), (617, 617)),
    ((1328, 1332), (618, 618)),
    ((1333, 1337), (619, 619)),
    ((1338, 1342), (621, 621)),
    ((1343, 1347), (623, 623)),
    ((1348, 1348), (624, 624)),
    ((1349, 1353), (626, 626)),
    ((1354, 1354), (627, 627)),
    ((1355, 1355), (628, 628)),
    ((1356, 1360), (630, 630)),
    ((1361, 1364), (633, 633)),
    ((1373, 1377), (638, 638)),
    ((1378, 1380), (641, 641)),
    ((1389, 1393), (651, 651)),
    ((1394, 1398), (652, 652)),
    ((1399, 1402), (655, 655)),
    ((1411, 1415), (659, 659)),
    ((1416, 1420), (660, 660)),
    ((1421, 1425), (662, 662)),
    ((1426, 1430), (664, 664)),
    ((1431, 1431), (665, 665)),
    ((1432, 1432), (669, 669)),
    ((1433, 1433), (670, 670)),
    ((1436, 1436), (672, 672)),
    ((1440, 1440), (673, 673)),
    ((1442, 1446), (675, 675)),
    ((1447, 1447), (676, 676)),
    ((1448, 1451), (679, 679)),
    ((1452, 1452), (680, 680)),
    ((1453, 1453), (681, 681)),
    ((1454, 1458), (683, 683)),
    ((1459, 1459), (685, 685)),
    ((1462, 1462), (686, 686)),
    ((1464, 1467), (689, 689)),
    ((1482, 1486), (694, 694)),
    ((1487, 1489), (697, 697)),
    ((1498, 1502), (702, 702)),
    ((1503, 1505), (705, 705)),
    ((1514, 1518), (712, 712)),
    ((1519, 1523), (713, 713)),
    ((1524, 1527), (716, 716)),
    ((1536, 1540), (720, 720)),
    ((1541, 1545), (721, 721)),
    ((1546, 1550), (722, 722)),
    ((1551, 1555), (724, 724)),
    ((1556, 1560), (725, 725)),
    ((1561, 1561), (726, 726)),
    ((1562, 1562), (730, 730)),
    ((1563, 1563), (731, 731)),
    ((1566, 1566), (733, 733)),
    ((1570, 1570), (734, 734)),
    ((1572, 1576), (736, 736)),
    ((1577, 1577), (737, 737)),
    ((1578, 1581), (740, 740)),
    ((1582, 1582), (741, 741)),
    ((1583, 1583), (743, 743)),
    ((1584, 1588), (745, 745)),
    ((1589, 1589), (747, 747)),
    ((1592, 1592), (748, 748)),
    ((1594, 1597), (751, 751)),
    ((1612, 1616), (755, 755)),
    ((1617, 1621), (756, 756)),
    ((1622, 1626), (758, 758)),
    ((1627, 1627), (759, 759)),
    ((1628, 1630), (762, 762)),
    ((1639, 1643), (767, 767)),
    ((1644, 1648), (768, 768)),
    ((1649, 1653), (770, 770)),
    ((1654, 1654), (771, 771)),
    ((1655, 1657), (774, 774)),
    ((1666, 1670), (778, 778)),
    ((1671, 1673), (782, 782)),
    ((1682, 1686), (787, 787)),
    ((1687, 1691), (788, 788)),
    ((1692, 1696), (789, 789)),
    ((1697, 1697), (791, 791)),
    ((1698, 1701), (793, 793)),
    ((1702, 1702), (794, 794)),
    ((1703, 1703), (797, 797)),
    ((1704, 1707), (799, 799)),
    ((1708, 1708), (800, 800)),
    ((1709, 1709), (801, 801)),
    ((1710, 1710), (803, 803)),
    ((1711, 1714), (805, 805)),
    ((1715, 1715), (806, 806)),
    ((1716, 1716), (807, 807)),
    ((1717, 1717), (809, 809)),
    ((1720, 1720), (810, 810)),
    ((1722, 1724), (812, 812)),
    ((1735, 1739), (821, 821)),
    ((1740, 1744), (822, 822)),
    ((1745, 1749), (824, 824)),
    ((1750, 1754), (825, 825)),
    ((1755, 1757), (827, 827)),
    ((1766, 1770), (833, 833)),
    ((1771, 1775), (834, 834)),
    ((1776, 1780), (836, 836)),
    ((1781, 1785), (837, 837)),
    ((1786, 1788), (839, 839)),
    ((1797, 1801), (843, 843)),
    ((1802, 1806), (844, 844)),
    ((1807, 1811), (846, 846)),
    ((1812, 1816), (847, 847)),
    ((1817, 1819), (849, 849)),
)
