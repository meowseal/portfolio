public class bee {

    private final int yearBorn;
    private int age;
    private int level;
    private String name;
    private int currentYear = 0;

    private static int beesEverMade = 0;


    public bee(int year)
    {
        level = 0;
        age = 0;
        currentYear = year;
        yearBorn = currentYear;
        beesEverMade ++;
        name = String.valueOf(beesEverMade);

        this.currentYear = currentYear;
    }

    public bee(int year, String name)
    {
        level = 0;
        age = 0;
        currentYear = year;
        yearBorn = currentYear;
        beesEverMade ++;
        this.name = name;

        this.currentYear = currentYear;
    }

    private static String getSprite(int age)
    {
        if (age < 2) {return color.cyan + "Baby";}
        if (age < 10) {return color.yellow +  "Worker";}
        else {return color.red + "Deceased";}
    }

    private static String getModifier(int age)
    {
        if (age < 2) {return color.cyan;}
        if (age < 10) {return color.yellow;}
        else {return color.red;}

    }

    public void newYear() {
        age ++;
        currentYear ++;

        if (age == 10) {System.out.println(getSprite(getAge() - 1) + color.reset + " bee " + name + " has died at year " + currentYear  + "\n");}


    }

    public int getAge()
    {
        if (age >= 10) {return 10;}
        else {return age;} 
    }
    public String toString()
    {
        return getSprite(getAge()) + color.reset + " bee " + name + " is " + getModifier(getAge()) + getAge() + color.reset + " years old and was born " + (currentYear - yearBorn) + " years ago" + "\n";
    }


}
