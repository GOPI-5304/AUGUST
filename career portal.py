# career portal.py

class CareerPage:
    def __init__(self):
        while True:
            print("welcome to all")
            print()
            print("enter admin")
            print("enter jobseeker")
            print()
            n = input("enter which you want : ")
            if n == 'admin':
                a = CareerPage.Admin()
            elif n == 'jobseeker':
                u = CareerPage.JobSeeker()
            else:
                print("inavalid entry ! try again later")

    class Admin:
        job_list = []
        seeker_details = []

        def __init__(self):
            # see all the posted jobs and add jobs 
            print("type add : to add the jobs by hr")
            print("type applications: to see the no of applications get received")
            
            n = input("enter add/applications : ")
            if n == 'add':
                self.add()
            elif n == 'application':
                self.applications()
            else:
                print(f"{n} jobs should not match the creerpage credentials")

        code = 1

        def add(self):
            d = {}
            d['reference-id'] = str(CareerPage.Admin.code)
            d['domain'] = input('Enter Domain : ')
            d['role'] = input('Enter role : ')
            d['location'] = input('Enter location : ')
            d['qualification'] = input('enter qualification : ')
            d['salary'] = input('Enter salary : ')
            d["description"]=input("enter description of job :" )
            CareerPage.Admin.job_list.append(d)
            CareerPage.Admin.code += 1
            print('Job post added succesfully')
            s = input('press enter to continue :')

        def applications(self):
            for d in CareerPage.Admin.seeker_details:
                print(d)
            else:
                s = input('press any key to continue')

    class JobSeeker(Admin):
        def __init__(self):
            for s in CareerPage.Admin.job_list:
                print(s)
            n = input('Enter reference id to  apply :')
            if n == '0':
                print("invalid reference id")
                p = input('press any key to continue : ')
            else:
                for s in CareerPage.Admin.job_list:
                    if n == s.get('reference id'):
                        d = {}
                        d['name'] = input('Enter your name: ')
                        d['mobile'] = input('enter mobile number: ')
                        d['age'] = input('Enter your age: ')
                        d['reference id'] = n
                        d['domain'] = s.get('domain')
                        CareerPage.Admin.seeker_details.append(d)
                        print(f"You have succesfully applied for the role of {s.get('Role')}")
                        s = input('press any key to continue')
                        break
                else:
                    print("Not found Error")
                    s = input('press enter to continue : ')


c = CareerPage()