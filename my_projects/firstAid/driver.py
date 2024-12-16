
import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

issue_goal = goal.compile('facts.diagnosed_decease($issue, $probability, $explanation)')
first_aid_goal = goal.compile('facts.first_aid($injury, $treatement)')
location_goal = goal.compile('facts.location_advice($issue,$advice)')




def fc_test():
    '''
        This function runs the forward-chaining example (fc_example.krb).
    '''
    engine.reset()  # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('fc')  # Put the name of the rule base here.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof \n")
    
    # Prove both goals
    with issue_goal.prove(engine) as gen1, first_aid_goal.prove(engine) as gen2, location_goal.prove(engine) as gen3:
        gen1_list = list(gen1)  # Convert gen1 to a list
        gen2_list = list(gen2)  # Convert gen2 to a list
        gen3_list = list(gen3)  # Convert gen3 to a list
        
        number_of_solutions = 0
        print("\n")
        for vars1, plan1 in gen1_list:
            if number_of_solutions>0:
                print("OR\n")
            # Print details of the issue
            print("\nYou may have %s issue."% (vars1['issue']), end=" ")
            if vars1['probability'] != 1:
                print("The probability of having the mentioned issue is %d%%" % (vars1['probability'] * 100))
            print("\n")
            if vars1['explanation'] != " ":
                print("This diagnosis was concluded:\n %s \n"% (vars1['explanation']))
            i = 0
            for vars2, plan2 in gen2_list:
                # Match vars1['issue'] with vars2['injury']
                if vars1['issue'] == vars2['injury']:
                    if i==0:
                        print("\nThe following is the treatment for your %s issue: \n Keep calm and follow the following procedure:\n" % \
                            (vars2['injury']))
                    if i>0:
                        print("OR \n")
                    print("%s" % \
                        (vars2['treatement']))
                    print("\n")
            
                    i+=1 
            for vars3, plan3 in gen3_list:
                if vars1['issue'] == vars3['issue']:
                    print("Location advice:\n%s" % vars3['advice'])
                    print("\n")  
                
            if i==0:
                missing_equip_goal = goal.compile('facts.missing_equipment($issue, $missing_equip_list)')
                print("\nyour current equipment are not enough to provide first aid for the diagnosed issue.")
                with missing_equip_goal.prove(engine) as gen4:
                    gen4_list = list(gen4)
                    for vars4, plan4 in gen4_list:
                        if vars1['issue'] == vars4['issue']:
                            print("You are missing the following equipment to provide first aid for your %s issue:" % vars4['issue'])
                            print(vars4['missing_equip_list'])
                            print("\n")
                        
            number_of_solutions += 1
            
        if number_of_solutions==0:
            print("\n")
            print("Sorry, there is not enough information to diagnose issue.")

        

    prove_time = time.time() - fc_end_time
    print()
    print("done")
    # engine.print_stats()
    print("fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('facts').get_stats()[2] / fc_time))




def bc_test():
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    try:
        with engine.prove_goal(
               'bc.diagnosed_decease($issue, $probability, $explanation)') \
          as gen:
            number_of_solutions = 0
            for vars, plan in gen:    
                if number_of_solutions>0:
                    print("OR\n")
                # Print details of the issue
                print("You may have %s issue."% (vars['issue']), end=" ")
                if vars['probability'] != 1:
                    print("The probability of having the mentioned issue is %d%%" % (vars['probability'] * 100))
                print("\n")
                if vars['explanation'] != " ":
                    print("This diagnosis was concluded:\n %s \n"% (vars['explanation']))
                

                    
                number_of_solutions += 1
            if number_of_solutions==0:
                print("\n")
                print("Sorry, there is not enough information to diagnose issue.")
                
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("execution finished.")
    

def bc_test_two():
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    try:
        with engine.prove_goal(
               'bc.diagnosed_decease($issue, $probability, $explanation)') \
          as gen1, engine.prove_goal(
               'bc.first_aid($injury, $treatement)') \
          as gen2:
            number_of_solutions = 0
            for vars1, plan in gen1:    
                if number_of_solutions>0:
                    print("OR")
                # Print details of the issue
                print("\n You may have %s issue."% (vars1['issue']), end=" ")
                if vars1['probability'] != 1:
                    print("The probability of having the mentioned issue is %d%%" % (vars1['probability'] * 100))
                print("\n")
                if vars1['explanation'] != " ":
                    print("This diagnosis was concluded:\n %s \n"% (vars1['explanation']))
                
                i = 0    
                for vars2, plan2 in gen2:
                    if vars1['issue'] == vars2['injury']:
                        if i==0:
                            print("\nThe following is the treatment for your %s issue: \n Keep calm and follow the following procedure:\n" % \
                                (vars2['injury']))
                        if i>0:
                            print("OR \n")
                        print("%s" % \
                            (vars2['treatement']))
                        print("\n")
                
                        i+=1
                with engine.prove_goal(
                        'bc.location_advice($issue, $advice)', issue=vars1['issue']) \
                as gen3:
                    gen3_list = list(gen3)
                    #print("gen3", gen3_list)
                    for vars3, plan3 in gen3_list:
                            if vars1['issue'] == vars3['issue']:
                                print("\nLocation advice:\n%s" % vars3['advice'])
                                print("\n")   
                if i==0:
                    print("\nyour current equipment are not enough to provide first aid for the diagnosed issue.")
                    with engine.prove_goal( 
                        'bc.missing_equipment($issue, $missing_equip_list)',
                        issue = vars1['issue']) \
                    as gen4:
                        gen4_list = list(gen4)
                        for vars4, plan4 in gen4_list:
                            if vars1['issue'] == vars4['issue']:
                                print("\nYou are missing the following equipment to provide first aid for your %s issue:" % vars4['issue'])
                                print(vars4['missing_equip_list'])
                                print("\n")
                

                    
                number_of_solutions += 1
            if number_of_solutions==0:
                print("\n")
                print("Sorry, there is not enough information to diagnose issue.")
                
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("execution finished.")
    
    
    
def bc_with_fc():
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print("doing proof")
    try:
        with engine.prove_goal(
               'bc.diagnosed_decease($issue, $probability, $explanation)') \
          as gen:
              

            
            number_of_solutions = 0
            for vars, plan in gen:    
                if number_of_solutions>0:
                    print("OR\n")
                # Print details of the issue
                print("You may have %s issue."% (vars['issue']), end=" ")
                if vars['probability'] != 1:
                    print("The probability of having the mentioned issue is %d%%" % (vars['probability'] * 100))
                print("\n")
                if vars['explanation'] != " ":
                    print("This diagnosis was concluded:\n %s \n"% (vars['explanation']))
                
                with first_aid_goal.prove(engine, injury = vars['issue']) as gen2, location_goal.prove(engine, issue = vars['issue']) as gen3:
                    
                    gen2_list = list(gen2)  # Convert gen2 to a list
                    gen3_list = list(gen3)  # Convert gen3 to a list
                    
                    i = 0
                    for vars2, plan2 in gen2_list:
                        # Match vars1['issue'] with vars2['injury']
                        #if vars['issue'] == injury:
                        if i==0:
                            print("The following is the treatment for your %s issue: \n Keep calm and follow the following procedure:\n" % \
                                (vars2['injury']))
                        if i>0:
                            print("OR \n")
                        print("%s" % \
                            (vars2['treatement']))
                        print("\n")
                        for vars3, plan3 in gen3_list:
                            print("Location advice:\n%s" % vars3['advice'])
                            print("\n")
                            i+=1   
                        
                    if i==0:
                        missing_equip_goal = goal.compile('facts.missing_equipment($issue, $missing_equip_list)')
                        print("your current equipment are not enough to provide first aid for the diagnosed issue.")
                        with missing_equip_goal.prove(engine) as gen4:
                            gen4_list = list(gen4)
                            #print(gen4_list)
                            for vars4, plan4 in gen4_list:
                                if vars['issue'] == vars4['issue']:
                                    print("You are missing the following equipment to provide first aid for your %s issue:" % vars4['issue'])
                                    print(vars4['missing_equip_list'])
                                    print("\n")               

                    
                number_of_solutions += 1
            if number_of_solutions==0:
                print("\n")
                print("Sorry, there is not enough information to diagnose issue.")
                
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print()
    print("execution finished.")



