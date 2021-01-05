#!/usr/bin/python 

def clear_list(list_ojb):

    BC_list = []
    BC_dict = {}
    BC_num = 0

    dict_ojb = {}
    duble_list1 = []
    duble_list2 = []
    in_clear_list = []
    for i in list_ojb:
        BC_num = BC_num + 1
        ojb_A,ojb_B = i.split('*')
        ojb_A_name,ojb_A_order = ojb_A.split('$')
        ojb_B_name,ojb_B_order = ojb_B.split('$')
        duble_str = '{}{}'.format(ojb_A,ojb_B_name)
        if ojb_A_name != ojb_B_name :
            BC_dict[BC_num] = i
            BC_list.append(ojb_A)
            ojb_A_and_ojb_B = '{}*{}'.format(ojb_A_name,ojb_B_name)
            if ojb_A_and_ojb_B not in duble_list1:
                dict_ojb['{}*{}'.format(ojb_A,ojb_B)] = max(int(ojb_A_order),int(ojb_B_order))
                duble_list1.append(ojb_A_and_ojb_B)
                duble_list2.append(duble_str)
            else:
                if duble_str not in duble_list2:
                    duble_list2.append(duble_str)
                    dict_ojb['{}*{}'.format(ojb_A,ojb_B)] = max(int(ojb_A_order),int(ojb_B_order))
        else:
            in_clear_list.append('{}${}-{}${}'.format(ojb_A_name,ojb_A_order,ojb_B_name,ojb_B_order))
                
    BC_list = list(set(BC_list))
    for key,value in BC_dict.items():
        A,B = value.split('*')
        if B in BC_list:
            ojb_A, ojb_B = value.split('*')
            ojb_A_name, ojb_A_order = ojb_A.split('$')
            ojb_B_name, ojb_B_order = ojb_B.split('$')
            dict_ojb['{}*{}'.format(ojb_A,ojb_B)] = max(int(ojb_A_order),int(ojb_B_order))

    new_dict_ojb = {v:k for k,v in dict_ojb.items()}
    finall_dict = {}
    num = 0
    for i in sorted(new_dict_ojb.keys()):
        num = num + 1
        finall_dict[num] = new_dict_ojb[i]

    for i in in_clear_list:
        A_target,B_target = i.split('-')
        str_dict = str(finall_dict).replace(A_target,B_target)

    return eval(str_dict)


test_list = ['A_a$1*B_b$2','B_b$2*B_b$3','B_b$2*I_i$17','B_b$3*C_c$4','B_b$3*G_g$15','B_b$3*H_h$16','C_c$4*D_d$5','C_c$4*D_d$7','C_c$4*D_d$12','D_d$5*E_e$6','D_d$7*E_e$8','D_d$7*E_e$9','D_d$7*E_e$11','E_e$9*F_f$10','D_d$12*F_f$13','D_d$12*E_e$14']
#test_list = ['A_a$1*B_b$2','B_b$2*B_b$3','B_b$2*H_h$14','B_b$3*C_c$4','B_b$3*F_f$12','B_b$3*G_g$13','C_c$4*D_d$5','C_c$4*D_d$9','D_d$5*E_e$6','D_d$5*E_e$7','D_d$5*E_e$8','D_d$9*F_f$10','D_d$9*E_e$11','E_e$11*Z_z$22']
result = clear_list(test_list)
print result
