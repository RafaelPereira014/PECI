
public interface ConsumerRecord<T1, T2> {

    Object offset();

    Object key();

    Object value();

}
