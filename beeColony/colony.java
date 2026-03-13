import java.util.ArrayList;

public class colony {

    private int year = 0;
    private ArrayList<bee> hive = new ArrayList<>();
    private double honeyProduced = 0;

    public void addBee()
    {
        bee Bee = new bee(year);
        hive.add(Bee);
    }

    public void addBee(String name)
    {
        bee Bee = new bee(year, name);
        hive.add(Bee);
    }





    public int hiveSize()
    {
        return hive.size();
    }

    public void nextYear()
    {
        for (bee Bee : hive) 
        {
            if (Bee.getAge() < 10) {
                honeyProduced += (Bee.getAge() * 80);
            }
            Bee.newYear();
        }

        year ++;
    }

    public String toString()
    {
        int beesAlive = 0;
        String string = color.green + "Hive Stats: \n" + color.reset;
        for (bee Bee : hive) 
        {
            if (Bee.getAge() < 10) {string += "   " + Bee.toString(); beesAlive ++;}

        }  
            if (beesAlive == 0)
            {
                string += color.red + "There are no bees in your hive" + color.reset;
            }
        
        string += "\nHoney produced: " + color.yellow + honeyProduced + color.reset + " mg";
        return string + "\n";
    }




}
