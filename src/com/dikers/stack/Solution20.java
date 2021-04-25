package com.dikers.stack;

public class Solution20 {

    public boolean isValid(String s) {

        Stack<Character> stack = new ArrayStack<>();

        if(s == null || s.length() == 0){
            return true;
        }


        for(int i=0; i<s.length() ;i++){
            Character c = s.charAt(i);

            if(c =='[' || c =='{' || c =='('){
                stack.push(c);
            }else {
                if(stack.isEmpty()){
                    return false;
                }

                char top = stack.pop();
                if(top == '[' && c !=']'){
                    return false;
                }else if(top =='{' && c!='}'){
                    return false;
                }else if(top =='(' && c!=')'){
                    return false;
                }
            }
        }
        return stack.isEmpty();

    }


    public static void main(String[] args) {

        Solution20 solution = new Solution20();

        System.out.println(solution.isValid("()[]{}"));
    }

}
