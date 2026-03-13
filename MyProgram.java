public class MyProgram
{
    public static void main(String[] args)
    {

        colony hive = new colony();
        System.out.print(hive);

        
        hive.addBee();
        hive.addBee("Riley");
        hive.nextYear();
        hive.nextYear();
        hive.addBee("Freddy");

        System.out.print(hive);
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        hive.addBee();
        hive.addBee();
        hive.addBee("Jimmy");
        System.out.print(hive);
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        System.out.print(hive);
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        hive.nextYear();
        System.out.print(hive);

    }
}