//
//  users.hpp
//  Smart Calendar DS
//
//  Created by apple on 1/29/19.
//  Copyright © 2019 apple. All rights reserved.
//

#ifndef users_hpp
#define users_hpp

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

class section;
class course;

class timeslot
{
public:
    timeslot();
    timeslot(int d, int s, int e): day(d), s_t(s), e_t(e) {}
    friend class course;
    void print();
private:
    int day;                    // 1 to 7 represents monday to sunday
    int s_t;                    // 4 digits number, first two is hour
    // last two is minutes
    int e_t;
    
};

class user{
public:
    user (string nm): money(0), user_name(nm), signature("") {}
    user(int m, string nm, string sig) : money(m), user_name(nm), signature(sig){}
    void set_money (int mon) { money = mon;}
    void add_money (int amt) { money += amt;}
    void set_name(string name) { user_name = name;}
    void set_signiture(string sig) { signature = sig;}
    // friend class course
    void c_register (course a_course);
    void print_sch();
    string get_nm() {return user_name;}
    string get_signature() {return signature;}
    //
private:
    int money;
    string user_name;
    string signature;
    vector<course> courses;
    // other user info here
};

class section{
public:
    section();
    section(string title_,string user_,string comment_):
    title(title_),user(user_),comment(comment_) {}
    void edit_tit (string new_t) {title = new_t;}
    void edit_comment (string new_c) {comment = new_c;}
    
private:
    string title;
    string user;
    string comment;
    
};


map<string, timeslot> set_weekly_sch();


class course{
public:
    course();
    course(string cnm, string inm): c_nm(cnm), i_nm(inm) {}
    course(string cnm, string inm, vector<timeslot> tm):
                c_nm(cnm), i_nm(inm), time(tm) {}
    void set_cnm(string cnm_) {c_nm = cnm_;}
    void set_inm(string inm_) {i_nm = inm_;}
    void add_comment (section c_sec);
    void add_classmate (user a_student) {classmates.push_back(a_student);}
    friend class timeslot;
    friend class user;
    void print();
private:
    string c_nm;
    string i_nm;
    vector<timeslot> time;
    vector<user> classmates;
    vector<section> comments;
};




#endif /* users_hpp */
