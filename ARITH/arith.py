def print_sum_or_diff(op1,op2,op):
    res = str(op1+op2) if op == "+" else str(op1-op2)
    op1 = str(op1)
    op2 = "+" + str(op2) if op == "+" else "-" + str(op2)
    max_len = max(len(res),len(op1),len(op2))
    dashes_len = max(len(res),len(op2))
    dashes = "-" * dashes_len
    print op1.rjust(max_len," ")
    print op2.rjust(max_len," ")
    print dashes.rjust(max_len," ")
    print res.rjust(max_len," ")
    print

def print_mult(op1,op2):
    partial_results = list()
    aux = str(op2)[::-1]
    res = str(op1*op2)
    for m in aux:
        partial_results.append(str(op1*int(m)))
    op1 = str(op1)
    op2 = "*" + str(op2)
    max_len = max(len(op1),len(op2),len(res))
    dashes_len = max(len(op2), len(partial_results[0]))
    dashes = "-" * dashes_len
    print op1.rjust(max_len," ")
    print op2.rjust(max_len," ")
    print dashes.rjust(max_len," ")
    for i in xrange(len(partial_results)):
        print partial_results[i].rjust(max_len-i," ")
    if len(partial_results) > 1:
        dashes_len = max(len(partial_results[-1]) + len(partial_results)-1,len(res))
        dashes = "-" * dashes_len
        print dashes.rjust(max_len," ")
        print res.rjust(max_len," ")
    print
    

def extract_operation(l):
    op = None
    for s in "+-*":
        if s in l:
            op = s
    op1, op2 = tuple(map(int,l.split(op)))
    return op1, op2, op

def main():
    t = input()
    for i in xrange(1, t+1):
        l = raw_input().strip()
        op1, op2, operator = extract_operation(l)
        if operator == "+" or operator == "-":
            print_sum_or_diff(op1, op2, operator)
        else:
            print_mult(op1, op2)

if __name__ == "__main__":
    main()
