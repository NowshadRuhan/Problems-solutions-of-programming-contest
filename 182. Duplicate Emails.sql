select email from person
group by email
having count(id) >=2